# 🧠 Math Agent: Agentic-RAG with Human-in-the-Loop Feedback

A smart educational assistant that replicates a math professor using Retrieval-Augmented Generation (RAG), WolframAlpha API, and robust guardrails to ensure educational quality, privacy, and feedback learning.

---

## 🚀 Features

- 🔍 **Knowledge Base Retrieval**: Uses cosine similarity to retrieve step-by-step math solutions from a custom vectorized knowledge base.
- 🌐 **Web Fallback (WolframAlpha API)**: When local knowledge fails, queries WolframAlpha for accurate computational results.
- 🛡️ **Input & Output Guardrails**:
  - Blocks non-mathematical inputs
  - Validates that the output is educational and math-relevant
  - Enforces privacy policies (no PII)
- 👤 **Human-in-the-Loop Feedback**:
  - Captures user feedback to improve accuracy
  - Future-ready for DSPy integration
- 📚 **Modular Design**: Easily extensible to other STEM fields or APIs.

---

## 🗂️ Project Structure

```bash
.
├── app.py                    # Main routing and execution logic
├── knowledge_base.json       # Sample mathematical Q&A dataset
├── retrieval/
│   └── vector_retriever.py   # Vector search with cosine similarity
├── guardrails/
│   ├── input_guardrails.py   # Math-related input filtering
│   ├── output_guardrails.py  # Output validation
│   └── privacy_guardrails.py # PII detection
├── human_feedback.py         # Collects and logs feedback
└── README.md                 # You're reading it!
