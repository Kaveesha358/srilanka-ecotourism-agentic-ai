# 🌿 Sri Lanka Eco-Tourism & Wildlife Agentic AI System

An intelligent multi-agent system designed for Sri Lanka Tourism to assist tourists and operators with Wildlife Conservation (DWC) regulations, Cultural Triangle guidelines, entrance fee calculations, and itinerary compliance validation.

---

## 📑 1. Project Description

The **Sri Lanka Eco-Tourism Agentic AI System** is an end-to-end AI assistant that combines Retrieval-Augmented Generation (RAG) with specialized agent workflow orchestration. It handles complex tourist queries by routing requests to specialized agents for rule retrieval, calculations, and regulatory compliance.

### Key Features
* **Smart Intent Routing:** Dynamically evaluates incoming user queries and routes them to appropriate agents.
* **Knowledge Retrieval (RAG):** Context-aware question answering based on official Sri Lanka Tourism & Wildlife documentation.
* **Automated Park Fee Calculator:** Accurate calculation of entry fees, vehicle charges, and VAT breakdown for national parks.
* **Compliance & Itinerary Inspector:** Checks proposed travel itineraries against official guidelines (e.g., dress codes, photography rules, wildlife safety).

---

## 🏗️ 2. Architecture Diagram

```mermaid
graph TD
    User[User Input] --> UI[Streamlit Interface]
    UI --> Router[Router Agent - Intent Detection]
    
    Router -->|Policy / Rules Query| Retriever[Retriever Agent - RAG Knowledge]
    Router -->|Park Fee Request| Calc[Calculator Tool - Fee Engine]
    Router -->|Itinerary Check| Comp[Compliance Agent - Policy Inspector]
    
    Retriever --> Final[Final Response]
    Calc --> Final
    Comp --> Final


## 🤖 3. Agent Communication Diagram

graph TD
    UserQuery["[User Query]"] --> Router[Router Agent]
    
    Router -->|Direct Answer| Final[Final Output]
    
    Router -->|Policy/Knowledge Query| Retriever["Retriever Agent<br/>(FAISS + MiniLM-L6)"]
    Retriever --> Final
    
    Router -->|Fee Calculation Request| Calc["Calculator Tool<br/>(LKR Rates + VAT)"]
    Calc --> Final
    
    Router -->|Itinerary Validation| Comp["Compliance Agent<br/>(Guidelines Check)"]
    Comp --> Final



    ## 🔄 4. Explanation of the RAG Pipeline

The Retrieval-Augmented Generation (RAG) pipeline enables accurate knowledge retrieval from official Sri Lanka tourism documents:

1. **Document Ingestion & Splitting:**
   * Official PDFs stored in `data/` (e.g., *Wildlife Tourism Guide*, *Cultural Guidelines*, *SLTDA Regulations*) are parsed using `PyPDFDirectoryLoader`.
   * Documents are split into semantic chunks using `RecursiveCharacterTextSplitter` with a chunk size of `1000` characters and an overlap of `150` characters.

2. **Vector Embeddings & Storage:**
   * Text chunks are embedded into dense vectors using the HuggingFace `all-MiniLM-L6-v2` model.
   * Embeddings are stored locally in a **FAISS** vector database (`vectorstore_db/`).

3. **Retrieval & Context Generation:**
   * When a query is passed to the Retriever Agent, the top k=3 most relevant document chunks are retrieved via similarity search.
   * The retrieved context is injected into the LLM system prompt to generate grounded, hallucination-free answers.

---

## 📊 5. Model Choice Comparison Table

| Feature / Metric | Groq (Llama 3.1 8B Instant) | OpenRouter (Qwen 2.5 72B) |
| :--- | :--- | :--- |
| **Primary Role** | Fast Routing & Basic Retrieval | Complex Reasoning & Compliance |
| **Latency** | Very Low (< 1 sec) | Moderate (~2-4 secs) |
| **Context Window** | 128k Tokens | 128k Tokens |
| **Cost Efficiency** | High (Inference Speed) | High (Quality relative to size) |
| **Task Suitability** | Intent Classification & Query Extraction | Multi-rule Validation & Itinerary Analysis |

---

## ⚙️ 6. Setup Instructions

### Prerequisites
* Python 3.10 or higher
* Git

### Installation Steps

1. **Clone the Repository:**
   ```bash
   git clone [https://github.com/Kaveesha358/srilanka-ecotourism-agentic-ai.git](https://github.com/Kaveesha358/srilanka-ecotourism-agentic-ai.git)
   cd srilanka-ecotourism-agentic-ai


   ## 🌐 7. Deliverables

   ### GitHub Repository: https://github.com/Kaveesha358/srilanka-ecotourism-agentic-ai/tree/main

   ### Live Streamlit App: https://srilanka-ecotourism-agentic-ai-2f3hh3bksi7ckwkwvvente.streamlit.app/