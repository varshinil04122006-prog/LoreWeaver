"""
LoreWeaver Multi-Agent System

Specialized agents:
1. Lore Agent
2. Continuity Agent
3. World-Building Agent
4. Narrative Agent
"""

def lore_agent(query, context, generator):

    prompt = f"""
You are the Lore Agent of LoreWeaver.

Identify established facts from the retrieved lore.

RETRIEVED LORE:
{context}

USER QUERY:
{query}

Do not invent facts.
Give a concise answer.
"""

    response = generator(prompt, max_new_tokens=80)

    return response[0]["generated_text"]


def continuity_agent(query, context, generator):

    prompt = f"""
You are the Continuity Agent of LoreWeaver.

Check the scenario against the established lore.

EXISTING LORE:
{context}

USER QUERY:
{query}

Check:
- Character consistency
- Timeline consistency
- Faction consistency
- Location consistency
- Contradictions

Give a concise continuity report.
"""

    response = generator(prompt, max_new_tokens=80)

    return response[0]["generated_text"]


def worldbuilding_agent(query, context, generator):

    prompt = f"""
You are the World-Building Agent of LoreWeaver.

Suggest logical extensions to the fictional universe.

EXISTING LORE:
{context}

USER QUERY:
{query}

Respect established facts and clearly treat new ideas as suggestions.
"""

    response = generator(prompt, max_new_tokens=100)

    return response[0]["generated_text"]


def narrative_agent(query, context, continuity_report, generator):

    prompt = f"""
You are the Narrative Agent of LoreWeaver.

Generate a short narrative continuation.

EXISTING LORE:
{context}

CONTINUITY REPORT:
{continuity_report}

USER QUERY:
{query}

Maintain character and world consistency.
Do not contradict established events.

Generate the narrative:
"""

    response = generator(prompt, max_new_tokens=150)

    return response[0]["generated_text"]
