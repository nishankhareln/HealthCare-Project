Patient → Streamlit Chat → FastAPI Backend → LangGraph Agent
                                ↓
                        ┌───────┴────────┐
                        ↓                ↓
                   PostgreSQL      ChromaDB (RAG)
                   (Doctors)       (Embeddings)

Simple FLow :
PATIENT
   ↓
   | (enters symptoms)
   ↓
STREAMLIT (Chat UI)
   ↓
   | (sends message)
   ↓
FASTAPI BACKEND
   ↓
   | (processes)
   ↓
LANGGRAPH AGENT
   ↓
   | (classifies urgency)
   ↓
   ├─→ HIGH → EMERGENCY ALERT
   |
   ├─→ MODERATE → SEARCH DOCTORS
   |                    ↓
   |               CHROMADB (finds doctors)
   |                    ↓
   |               POSTGRESQL (gets details)
   |                    ↓
   |               SHOW DOCTOR CARDS
   |
   └─→ LOW → AI ASSISTANT (general advice)
