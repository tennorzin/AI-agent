# AI Agent Dashboard - Web Search and Information Extraction

## Overview
The **AI Agent Dashboard** allows users to upload a CSV file, define a query, and retrieve structured information from the web using AI-powered tools. It leverages **SerpAPI** for web search and **OpenAI GPT** for information extraction. The app is built with **Streamlit** and allows users to extract structured information for entities listed in a CSV file.

## Features
- Upload a CSV file and preview its content.
- Select a column containing entities for search.
- Define a custom query with placeholders (`{entity}`) for entity-specific searches.
- Retrieve structured information by querying web results.
- Extract information using GPT and display results.
- Download the extracted information in CSV format.

## Technologies Used
- **Streamlit**: A Python library for creating web apps.
- **SerpAPI**: Provides search results from Google.
- **OpenAI GPT**: Used to extract meaningful information from search results.
- **Pandas**: Used for managing and displaying CSV data.

## Installation

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/ai-agent-dashboard.git
cd ai-agent-dashboard
