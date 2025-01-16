# Multi-Agent Collaboration Demo UI

A Streamlit-based user interface for multi agent collaboration demos. Each demo showcases different specialized agents working together to accomplish complex tasks.

## Available Demos

The following demos are supported and can be found in their respective folders:

- **Portfolio Assistant** (`/portfolio_assistant_agent/`): Analyzes stock tickers
- **Actor Critic Demo** (`/team_poems_agent/`): Demonstrates actor-critic pattern through poems
- **Sports Team Poet** (`/team_poems_agent/`): Creates poems about sports teams
- **Trip Planner** (`/trip_planner_agent/`): Generates travel itineraries
- **Voyage Virtuoso** (`/voyage_virtuoso_agent/`): Provides exotic travel recommendations
- **Mortgages Assistant** (`/mortgage_assistant/`): Handles mortgage-related queries

## Prerequisites

1. Follow the setup instructions in each agent's respective folder before using them in the demo UI:
   - `/mortgage_assistant/README.md`
   - `/voyage_virtuoso_agent/README.md`
   - `/trip_planner_agent/README.md`
   - etc.

2. Ensure you have:
   - Python 3.x
   - AWS credentials configured with appropriate permissions

3. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Running the Demo

1. Configure your AWS credentials with appropriate permissions

2. Run the Streamlit application:
   ```bash
   streamlit run demo-ui.py
   ```

3. Optionally, specify a specific bot using the BOT_NAME environment variable:
   ```bash
   BOT_NAME="<bot-name>" streamlit run demo-ui.py
   ```

   Supported BOT_NAME values:
   - "Portfolio Assistant" 
   - "Actor Critic Demo"
   - "Sports Team Poet"
   - "Trip Planner"
   - "Voyage Virtuoso"
   - "Mortgages Assistant" (default)

## Usage

1. The UI will display the selected bot's interface (defaults to Mortgages Assistant if not specified)
2. Enter your query in the chat input field
3. The agent will:
   - Process your request
   - Show the collaboration between different agents
   - Display thought processes and tool usage
   - Provide a detailed response

## Architecture

The demo UI integrates with Amazon Bedrock Agent Runtime for agent execution and showcases multi-agent collaboration features including:

- Dynamic routing between specialized agents
- Knowledge base lookups
- Tool invocations
- Code interpretation capabilities

Below is an example of the demo UI in action, showing the Mortgages Assistant interface:

![Demo UI Screenshot](demo-ui-mortgage.png)
