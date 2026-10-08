# 🐍 Python Server Guide for Node.js Developers

> Everything you need to understand Python servers, mapped to concepts you already know.

---

## 1. Express.js → FastAPI (Side-by-Side)

### Creating the App

```javascript
// Node.js (Express)
const express = require('express');
const app = express();
app.listen(3000);
```

```python
# Python (FastAPI)
from fastapi import FastAPI
app = FastAPI()
# Start with: uvicorn app.main:app --reload --port 8000
```

### Defining Routes

```javascript
// Express
router.get('/users/:id', (req, res) => {
    res.json({ id: req.params.id });
});
```

```python
# FastAPI
@router.get("/users/{id}")
async def get_user(id: int):  # auto-validates that id is an integer!
    return {"id": id}
```

### Middleware

```javascript
// Express
app.use(cors());
app.use(express.json());  // ← FastAPI does this automatically
app.use(errorHandler);
```

```python
# FastAPI
app.add_middleware(CORSMiddleware, allow_origins=["*"])
# JSON parsing is automatic — no body-parser needed!
app.add_exception_handler(Exception, error_handler)
```

### Request Body Validation

```javascript
// Express + Joi
const schema = Joi.object({ url: Joi.string().required() });
app.post('/summarize', validate(schema), handler);
```

```python
# FastAPI + Pydantic (built-in, no extra library!)
class SummarizeRequest(BaseModel):
    url: str  # required by default, auto-validated

@app.post("/summarize")
async def summarize(req: SummarizeRequest):  # auto-validates!
    return {"url": req.url}
```

---

## 2. Key Differences You'll Notice

| Concept | Node.js | Python |
|---------|---------|--------|
| Package manager | `npm` / `yarn` | `pip` / `uv` |
| Config file | `package.json` | `pyproject.toml` |
| Dependencies folder | `node_modules/` | `.venv/` (virtual environment) |
| Run dev server | `nodemon server.js` | `uvicorn app.main:app --reload` |
| Router | `express.Router()` | `APIRouter()` |
| Validation | Joi / Zod / Yup | Pydantic (built into FastAPI) |
| Env variables | `dotenv` + `process.env` | `python-dotenv` + `os.getenv()` |
| Auto API docs | Swagger (manual setup) | **FREE** at `/docs` (auto-generated!) |
| Type safety | TypeScript (optional) | Type hints (optional but encouraged) |
| Async | `async/await` (native) | `async/await` (same syntax!) |
| Hot reload | `nodemon` | `--reload` flag in uvicorn |

---

## 3. File Structure Comparison

```
Node.js Express                     Python FastAPI
──────────────────                  ──────────────────
server.js                           app/main.py
routes/                             app/modules/
  ├── userRoutes.js                   ├── week1.py
  └── authRoutes.js                   └── week2.py
services/                           app/services/
  ├── userService.js                  ├── scraper.py
  └── emailService.js                 └── llm_client.py
middleware/                          app/middleware/
  └── errorHandler.js                 └── error_handler.py
config/                              app/config.py
  └── index.js
models/                              (Pydantic models inline or
  └── User.js                         in a models/ folder)
package.json                         pyproject.toml
.env                                 .env
node_modules/                        .venv/
```

---

## 4. Common Commands Translation

| What you want to do | Node.js | Python (with uv) |
|---------------------|---------|-------------------|
| Install dependencies | `npm install` | `uv sync` |
| Add a package | `npm install axios` | `uv add httpx` |
| Run dev server | `npm run dev` | `uvicorn app.main:app --reload` |
| Run a script | `node script.js` | `python script.py` |
| Format code | `prettier` | `black` or `ruff format` |
| Lint code | `eslint` | `ruff` or `flake8` |
| Run tests | `jest` or `mocha` | `pytest` |

---

## 5. Python-Specific Things to Know

### Virtual Environments (like a per-project node_modules)
```bash
# Node.js installs per-project automatically.
# Python needs a "virtual environment":
python -m venv .venv        # create it (already done for you)
source .venv/bin/activate   # activate it (Mac/Linux)
# Now `pip install` goes into .venv/ instead of global
```

### `__init__.py` Files
Every folder that contains importable Python code needs an `__init__.py` file.
Think of it like `index.js` — it tells Python "this folder is a package."

### Indentation Matters
Python uses indentation instead of `{ }` braces:
```python
# This is how blocks work — no braces, just indent
if True:
    print("inside if")     # 4 spaces = inside the block
print("outside if")        # back to 0 spaces = outside
```

### No Semicolons, No `const/let/var`
```javascript
// JavaScript
const name = "hello";
let count = 0;
```
```python
# Python — just assign
name = "hello"
count = 0
```

---

## 6. FastAPI Superpowers (Things Express Doesn't Give You for Free)

### 🎁 Auto-Generated API Docs
Visit `http://localhost:8000/docs` and you get a full **Swagger UI** for free.
Every route, every request body, every response — documented and testable.
No Swagger setup needed. It just works.

### 🎁 Auto Validation
Define a Pydantic model and FastAPI validates every request automatically.
Bad request? It returns a clean 422 error with details. No Joi/Zod needed.

### 🎁 Type Hints = Documentation
```python
@app.get("/items/{item_id}")
async def read_item(item_id: int, q: str = None):
    # item_id is guaranteed to be an int
    # q is an optional query parameter
    return {"item_id": item_id, "q": q}
```

---

## 7. 🤔 Is This How Real LLM Engineers Work?

**Honest answer: Not exactly, but your approach has real value.**

### How Real LLM Engineers Actually Work

| Phase | Tool | Why |
|-------|------|-----|
| **Experimenting** | Jupyter Notebooks (`.ipynb`) | Quick iteration, see results inline, visual output |
| **Prototyping** | Python scripts + CLI | Faster than setting up a server |
| **Production APIs** | FastAPI / Flask | When the model needs to serve real users |
| **ML Training** | Notebooks + Colab/Cloud GPUs | Heavy compute, visual monitoring |
| **Deployment** | Docker + Cloud (AWS/GCP) | Scaling to handle real traffic |

### The Typical LLM Engineer Workflow
1. **Explore** in Jupyter notebooks (90% of early work)
2. **Refactor** working code into Python modules/scripts
3. **Wrap** in FastAPI only when you need an API endpoint
4. **Deploy** with Docker to cloud

### Why Your FastAPI Approach Is Actually GREAT for Learning

> **As a Node.js developer, you're doing something smart.** You're mapping unfamiliar concepts (Python, ML, LLMs) onto a mental model you already understand (server, routes, services). This is a valid and effective learning strategy.

Here's why it works for you:

| ✅ Advantage | Why |
|-------------|-----|
| Familiar structure | Routes, services, middleware — you know this pattern |
| Testable endpoints | Hit `/week1/summarize` with Postman/curl like you would in Node |
| Progressive learning | Each week is a new module, visible in your server |
| API-first thinking | In production, LLMs ARE served via APIs — you're learning the real pattern |
| Portfolio-ready | "I built an 8-module AI API server" looks great on a resume |

### What Real LLM Engineers Would Add on Top
When you're ready to go deeper:
- **Notebooks** for data exploration & model evaluation
- **Async processing** for long-running tasks (fine-tuning, batch inference)
- **Caching** (Redis) for repeated LLM calls
- **Rate limiting** for API cost control
- **Logging & monitoring** (Weights & Biases, LangSmith)

### Bottom Line
> Notebooks are the industry standard for exploration. But **wrapping LLM logic in a FastAPI server is exactly what production LLM engineers do.** You're just doing it from Day 1 instead of Day 100. That's not wrong — that's efficient. 🚀

---

## 8. Quick Start

```bash
# From the project root:
cd llm_engineering

# Start the server (like: nodemon server.js)
uvicorn app.main:app --reload

# Visit in browser:
open http://localhost:8000        # Root — server status
open http://localhost:8000/docs   # Swagger UI (your new best friend!)

# Test with curl (like Postman):
curl http://localhost:8000/week1/health

curl -X POST http://localhost:8000/week1/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Explain Python in 3 sentences"}'
```

---

*Written for Node.js developers learning Python & LLM Engineering. 🤝*
