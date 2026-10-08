# 📚 LLM Engineering — Course Modules (All 8 Weeks)

> Each week builds on the previous one, culminating in a full Agentic AI system in Week 8.

---

## Week 1 — LLM APIs & Prompt Engineering
**Goal:** Make your first LLM API call and understand prompting.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | OpenAI API Basics | API keys, chat completions, first LLM call |
| 2 | Multi-Model Intro | Gemini, Claude, Ollama — same pattern, different providers |
| 3 | Prompt Engineering | System prompts, user prompts, temperature, tokens |
| 4 | Web Scraping + AI | BeautifulSoup, feeding real data to LLMs |
| 5 | Gradio UI | Building a simple web interface for your LLM |

**API Endpoint:** `POST /week1/summarize`, `POST /week1/chat`

---

## Week 2 — Multi-Model & Conversation Chains
**Goal:** Compare models and build multi-turn conversations.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | Comparing Frontier Models | GPT vs Claude vs Gemini — strengths & weaknesses |
| 2 | Multi-Turn Conversations | Message history, context windows, memory |
| 3 | Streaming Responses | Server-sent events, real-time token output |
| 4 | Model Routing | Picking the best model per task type |
| 5 | Multi-Model Chatbot | UI that lets you switch models on the fly |

**API Endpoint:** `POST /week2/compare`, `POST /week2/chat-stream`

---

## Week 3 — Embeddings & Vector Databases
**Goal:** Understand how text becomes numbers and why that matters.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | What Are Embeddings? | Text → vectors, semantic meaning |
| 2 | ChromaDB Setup | Local vector database, storing embeddings |
| 3 | Semantic Search | Vector similarity vs keyword matching |
| 4 | Similarity Scoring | Cosine similarity, nearest neighbors |
| 5 | Semantic Search API | Full search endpoint with ranking |

**API Endpoint:** `POST /week3/embed`, `POST /week3/search`

---

## Week 4 — RAG (Retrieval-Augmented Generation)
**Goal:** Build an AI that answers questions using YOUR documents.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | Why RAG? | LLM knowledge cutoffs, hallucination prevention |
| 2 | Document Loading | PDFs, text files, web pages → chunks |
| 3 | Text Splitting | Chunk size, overlap, recursive splitting |
| 4 | Retrieval + Generation | Combining search results with LLM prompts |
| 5 | Full RAG Q&A System | End-to-end question-answering pipeline |

**API Endpoint:** `POST /week4/ingest`, `POST /week4/ask`

---

## Week 5 — LangChain & Agents
**Goal:** Build AI agents that can use tools autonomously.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | LangChain Basics | Chains, prompts, output parsers |
| 2 | Tools & Function Calling | Giving LLMs access to APIs, calculators, search |
| 3 | Building Agents | ReAct pattern, autonomous decision-making |
| 4 | Agent Memory | Short-term vs long-term memory, conversation buffers |
| 5 | Multi-Tool Agent | Agent that searches, calculates, and browses |

**API Endpoint:** `POST /week5/agent`, `POST /week5/tools`

---

## Week 6 — Fine-Tuning LLMs
**Goal:** Customize a model on your own data.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | When to Fine-Tune | Prompting vs RAG vs fine-tuning decision tree |
| 2 | Hugging Face Ecosystem | Transformers, datasets, model hub |
| 3 | LoRA & QLoRA | Efficient fine-tuning without massive GPUs |
| 4 | Training on Custom Data | Google Colab, training loop, evaluation |
| 5 | Deploying Your Model | Saving, loading, serving fine-tuned models |

**API Endpoint:** `POST /week6/train`, `GET /week6/model-status`

---

## Week 7 — Evaluation, Testing & Cost Optimization
**Goal:** Make your LLM apps production-ready.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | Evaluating LLM Outputs | BLEU, ROUGE, human eval, LLM-as-judge |
| 2 | Automated Testing | Test suites for LLM applications |
| 3 | Cost Tracking | Token usage, API spend monitoring |
| 4 | Guardrails & Safety | Content filters, output validation |
| 5 | Production Pipeline | CI/CD for LLM apps, monitoring |

**API Endpoint:** `POST /week7/evaluate`, `GET /week7/costs`

---

## Week 8 — Agentic AI: The Capstone 🎓
**Goal:** Build a full autonomous AI agent system.

| Day | Topic | Key Concepts |
|-----|-------|--------------|
| 1 | Agentic AI Architecture | Patterns: ReAct, Plan-and-Execute, Multi-Agent |
| 2 | Multi-Agent Systems | Agents that delegate to other agents |
| 3 | Tool Orchestration | Dynamic tool selection, error recovery |
| 4 | Building the Capstone | Full autonomous agent with memory + tools |
| 5 | Deployment & Presentation | Deploying to production, final demo |

**API Endpoint:** `POST /week8/agent`, `GET /week8/status`

---

## Quick Reference

| Week | Theme | Status |
|------|-------|--------|
| 1 | LLM APIs & Prompts | ✅ Implemented |
| 2 | Multi-Model & Chains | 🚧 Placeholder |
| 3 | Embeddings & Vector DB | 🚧 Placeholder |
| 4 | RAG Pipeline | 🚧 Placeholder |
| 5 | LangChain & Agents | 🚧 Placeholder |
| 6 | Fine-Tuning | 🚧 Placeholder |
| 7 | Evaluation & Cost | 🚧 Placeholder |
| 8 | Agentic AI (Capstone) | 🚧 Placeholder |
