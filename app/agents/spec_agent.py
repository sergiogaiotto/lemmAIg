from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage, HumanMessage
from langgraph.graph import StateGraph, START, END
from typing import TypedDict, Annotated
from operator import add

from app.core.config import OPENAI_API_KEY, MODEL_NAME
from app.core.prompts import (
    SPECIFY_SYSTEM,
    PLAN_SYSTEM,
    TASKS_SYSTEM,
    IMPLEMENT_SYSTEM,
)
from app.services.project_service import read_file_safe, get_project_dir


class AgentState(TypedDict):
    messages: Annotated[list, add]
    phase: str
    project_name: str
    output: str


def _get_llm() -> ChatOpenAI:
    return ChatOpenAI(
        model=MODEL_NAME,
        api_key=OPENAI_API_KEY,
        temperature=0.3,
    )


def specify_node(state: AgentState) -> dict:
    llm = _get_llm()
    response = llm.invoke(
        [SystemMessage(content=SPECIFY_SYSTEM)] + state["messages"]
    )
    return {"output": response.content, "messages": [response]}


def plan_node(state: AgentState) -> dict:
    llm = _get_llm()
    project_dir = get_project_dir(state["project_name"])
    espec = read_file_safe(project_dir / "ESPEC.md")
    context = f"## ESPEC.md existente:\n\n{espec}\n\n"
    messages = [
        SystemMessage(content=PLAN_SYSTEM),
        HumanMessage(content=context),
    ] + state["messages"]
    response = llm.invoke(messages)
    return {"output": response.content, "messages": [response]}


def tasks_node(state: AgentState) -> dict:
    llm = _get_llm()
    project_dir = get_project_dir(state["project_name"])
    espec = read_file_safe(project_dir / "ESPEC.md")
    dp = read_file_safe(project_dir / "DP.md")
    context = f"## ESPEC.md:\n\n{espec}\n\n## DP.md:\n\n{dp}\n\n"
    messages = [
        SystemMessage(content=TASKS_SYSTEM),
        HumanMessage(content=context + "Gere a lista de tarefas."),
    ]
    response = llm.invoke(messages)
    return {"output": response.content, "messages": [response]}


def implement_node(state: AgentState) -> dict:
    llm = _get_llm()
    project_dir = get_project_dir(state["project_name"])
    espec = read_file_safe(project_dir / "ESPEC.md")
    dp = read_file_safe(project_dir / "DP.md")
    tasks = read_file_safe(project_dir / "TASKS.md")
    context = (
        f"## ESPEC.md:\n\n{espec}\n\n"
        f"## DP.md:\n\n{dp}\n\n"
        f"## TASKS.md:\n\n{tasks}\n\n"
    )
    messages = [
        SystemMessage(content=IMPLEMENT_SYSTEM),
        HumanMessage(content=context),
    ] + state["messages"]
    response = llm.invoke(messages)
    return {"output": response.content, "messages": [response]}


def route_phase(state: AgentState) -> str:
    return state["phase"]


def build_spec_graph() -> StateGraph:
    graph = StateGraph(AgentState)

    graph.add_node("specify", specify_node)
    graph.add_node("plan", plan_node)
    graph.add_node("tasks", tasks_node)
    graph.add_node("implement", implement_node)

    graph.add_conditional_edges(START, route_phase, {
        "specify": "specify",
        "plan": "plan",
        "tasks": "tasks",
        "implement": "implement",
    })

    graph.add_edge("specify", END)
    graph.add_edge("plan", END)
    graph.add_edge("tasks", END)
    graph.add_edge("implement", END)

    return graph.compile()


spec_graph = build_spec_graph()


async def run_phase(phase: str, project_name: str, user_input: str) -> str:
    result = spec_graph.invoke({
        "messages": [HumanMessage(content=user_input)],
        "phase": phase,
        "project_name": project_name,
        "output": "",
    })
    return result["output"]
