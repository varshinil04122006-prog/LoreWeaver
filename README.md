# 🧙 LoreWeaver

## Generative Multi-Agentic RAG Engine for Real-Time Narrative Continuity and World-Building

LoreWeaver is an AI-powered narrative intelligence prototype that uses **Retrieval-Augmented Generation (RAG)** and a lightweight **multi-agent architecture** to generate lore-grounded and continuity-aware stories for fictional game universes.

## 🎯 Problem

Large gaming and multimedia universes contain thousands of interconnected characters, locations, factions, and events. Generative AI can accidentally create contradictions with established lore.

LoreWeaver addresses this by retrieving relevant existing lore before generating new narrative content.

## 💡 Solution

```text
User Query
    ↓
Query Embedding
    ↓
FAISS Vector Database
    ↓
Relevant Lore Retrieval
    ↓
Multi-Agent Processing
    ↓
┌─────────────────────────┐
│ Lore Agent              │
│ Continuity Agent        │
│ World-Building Agent    │
│ Narrative Agent         │
└─────────────────────────┘
    ↓
Final Narrative
    ↓
Gradio Interface
