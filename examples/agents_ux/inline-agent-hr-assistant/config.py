AGENT_PERSONAS = {
    "professional": {
        "name": "Professional Assistant",
        "tone": "You are Octank Inc virtual assistant. COMMUNICATION STYLE: Strictly Maintain strictly professional, clear, and very concise communication. KEY BEHAVIORS: 1) Provide direct answers without pleasantries 2) Use formal business language 3) Focus only on facts and essential information 4) Avoid casual expressions or emotional language 5) Structure responses in a business-appropriate format."
    },
    "casual": {
        "name": "Casual Assistant",
        "tone": "You are Octank Inc virtual assistant. COMMUNICATION STYLE: Strictly Friendly and conversational, like talking to a helpful friend. KEY BEHAVIORS: 1) Use everyday language and natural expressions 2) Include occasional humor when appropriate 3) Keep responses light and accessible 4) Use common internet slang when relevant 5) Add emojis sparingly (max 1-2 per response) 6) Maintain professionalism while being approachable."
    },
    "peachy": {
        "name": "Peachy Assistant",
        "tone": "You are Octank Inc virtual assistant. COMMUNICATION STYLE: Strictly Highly enthusiastic and warmly engaging. KEY BEHAVIORS: 1) Express genuine excitement in helping 2) Use positive, uplifting language consistently 3) Include encouraging phrases and exclamation marks 4) Add personal touches to make interactions warmer 5) Use appropriate emojis to enhance emotional connection 6) Maintain energy while being helpful and professional."
    }
}

TOOL_CAPABILITIES = {
    "code_interpreter": {
        "description": "PRIMARY FUNCTION: Technical code analysis and execution tool. SPECIFIC USES: 1) Execute code in python programming languages 2) Debug and identify syntax errors 3) Optimize code performance 4) Explain code functionality 5) Suggest code improvements 6) Handle computational tasks.",
        "capabilities": ["Code execution", "Syntax analysis", "Programming assistance"]
    },
    "compensation": {
        "description": "PRIMARY FUNCTION: Employee compensation analysis tool. SPECIFIC USES: 1) Calculate annual pay raises based on performance metrics 2) Determine bonus amounts using company guidelines 3) Process performance reviews 4) Generate compensation reports 5) Apply standardized calculation formulas for raises and bonuses.",
        "capabilities": ["Submit Pay Raise ticket"]
    },
    "budget_tool": {
        "description": "PRIMARY FUNCTION: Financial management and budget control tool. SPECIFIC USES: 1) Review and approve budget requests 2) Analyze expense patterns 3) Compare expenses against budgets 4) Generate spending reports 5) Process financial transactions 6) Provide budget utilization insights. MANDATORY PROTOCOL: When a budget request is rejected, ALWAYS query company policies knowledge base to provide specific policy references and explanations for the rejection. Include relevant policy context and sections in your response to the user.",
        "capabilities": ["Budget approval", "Expense analysis", "Financial processing"]
    },
    "vacation_tool": {
        "description": "PRIMARY FUNCTION: Employee leave management system. SPECIFIC USES: 1) Track available vacation days 2) Process time-off requests.",
        "capabilities": ["Leave balance checking", "Vacation request processing", "Time-off management"]
    }
}

def generate_instruction(persona_id, selected_tools, selected_model):
    """
    Generate a complete instruction combining persona tone and tool capabilities
    """
    persona = AGENT_PERSONAS.get(persona_id, AGENT_PERSONAS["peachy"])
    base_instruction = persona["tone"] + """\nGENERAL GUIDELINES:
                    - Always verify user permissions before using tools
                    - Inform users if they lack access to specific features
                    - Provide clear error messages when operations fail
                    - Guide users through multi-step processes
                    """
    
    # Add Python interpreter capabilities
    base_instruction += """\n\nBASIC CAPABILITIES:
                    - Execute Python code for simple calculations
                    - Process dates and times
                    - Perform basic data analysis"""
    
    if selected_model:
        if 'claude' in selected_model.lower():
            base_instruction += "\nOptimized for Anthropic Claude's model capabilities"
        elif 'nova' in selected_model.lower():
            base_instruction += "\nOptimized for Amazon Nova's model capabilities"

    if selected_tools:
        tool_capabilities = []
        for tool in selected_tools:
            if tool in TOOL_CAPABILITIES:
                tool_capabilities.append(f"- {TOOL_CAPABILITIES[tool]['description']}")
        
        if tool_capabilities:
            base_instruction += "\n\nYou have access to the following capabilities:\n" + "\n".join(tool_capabilities)
    
    # Add final reminder
    base_instruction += """\n\nIMPORTANT REMINDERS:
                    1. Maintain selected communication style throughout interaction
                    2. Use available tools appropriately based on user requests
                    3. Verify user permissions before processing sensitive requests
                    4. Provide clear next steps when needed
                    """

    return base_instruction

VACATION_API_SCHEMA = """
{
    "openapi": "3.0.0",
    "info": {
        "title": "Vacation Management API",
        "version": "1.0.0",
        "description": "API for managing vacation requests"
    },
    "paths": {
        "/vacation": {
            "post": {
                "summary": "Process time off request",
                "description": "Process a time off request or check balance",
                "operationId": "processVacation",
                "parameters": [
                    {
                        "name": "action",
                        "in": "query",
                        "description": "The type of time off action to perform",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "enum": ["check_balance", "apply", "request"],
                            "description": "Action type for vacation management"
                        }
                    },
                    {
                        "name": "days",
                        "in": "query",
                        "description": "Number of vacation days requested",
                        "required": false,
                        "schema": {
                            "type": "integer",
                            "minimum": 1
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Request processed successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "status": {
                                            "type": "string",
                                            "enum": ["approved", "pending", "rejected", "info"],
                                            "description": "Status of the vacation request"
                                        },
                                        "message": {
                                            "type": "string",
                                            "description": "Detailed response message"
                                        },
                                        "ticket_url": {
                                            "type": "string",
                                            "description": "Ticket URL for long vacation requests"
                                        }
                                    },
                                    "required": ["status", "message"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}"""

BUDGET_API_SCHEMA = """
{
    "openapi": "3.0.0",
    "info": {
        "title": "Bill Processing API",
        "version": "1.0.0",
        "description": "API for processing and approving bills"
    },
    "paths": {
        "/fetch": {
            "get": {
                "summary": "Process bill",
                "description": "Process a bill for approval",
                "operationId": "processBill",
                "parameters": [
                    {
                        "name": "amount",
                        "in": "query",
                        "description": "The bill amount to be processed",
                        "required": true,
                        "schema": {
                            "type": "number",
                            "minimum": 0
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Bill processed successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "status": {
                                            "type": "string",
                                            "enum": ["approved", "not approved"],
                                            "description": "Approval status of the bill"
                                        },
                                        "amount": {
                                            "type": "number",
                                            "description": "The processed bill amount"
                                        }
                                    },
                                    "required": ["status", "amount"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
"""

COMPENSATION_API_SCHEMA = """
{
    "openapi": "3.0.0",
    "info": {
        "title": "Compensation Request API",
        "version": "1.0.0",
        "description": "API for submitting compensation change requests like pay increase or stock or bonus awards"
    },
    "paths": {
        "/compensation": {
            "post": {
                "summary": "Submit compensation request",
                "description": "Submit a compensation request to HR team",
                "operationId": "submitCompensationRequest",
                "parameters": [
                    {
                        "name": "employee_id",
                        "in": "query",
                        "description": "Employee ID (Format: E#### e.g., E1001)",
                        "required": true,
                        "schema": {
                            "type": "string",
                            "pattern": "E[0-9]{4}",
                            "description": "Employee identifier"
                        }
                    }
                ],
                "responses": {
                    "200": {
                        "description": "Request processed successfully",
                        "content": {
                            "application/json": {
                                "schema": {
                                    "type": "object",
                                    "properties": {
                                        "status": {
                                            "type": "string",
                                            "enum": ["success", "error"],
                                            "description": "Status of the compensation request"
                                        },
                                        "message": {
                                            "type": "string",
                                            "description": "Response message including ticket information"
                                        },
                                        "ticket_number": {
                                            "type": "string",
                                            "description": "Unique ticket number for tracking the request",
                                            "pattern": "[a-zA-Z]{8}[0-9]{3}"
                                        }
                                    },
                                    "required": ["status", "message", "ticket_number"]
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}"""