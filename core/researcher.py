from duckduckgo_search import DDGS

def get_company_info(company_name):
    """
    Searches DuckDuckGo for the company's mission and culture.
    Returns a summarized string of the top results.
    """
    if not company_name or company_name.lower() == "unknown":
        return "No company name found to research."

    print(f"   🕵️  Researching '{company_name}'...")
    
    query = f"{company_name} company mission values culture latest news"
    
    try:
        # Get top 3 text results
        results = DDGS().text(query, max_results=3)
        
        if not results:
            return "No external information found."
            
        # Combine snippets into one text block
        summary = "\n".join([f"- {r['body']}" for r in results])
        return summary

    except Exception as e:
        print(f"   ⚠️ Search Error: {e}")
        return "Search failed, using Job Description only."