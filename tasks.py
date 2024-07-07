from crewai import Task

class WebsiteAutomationTask():
    def css_selector_test_case_writing(self, agent):
        return Task(
            description=#"""Analyze the website structure and create detailed test cases for every Element Name. 
                           #Include positive and negative scenarios, edge cases, and cross-browser compatibility checks.""",
                           """Analyze the website structure and create detailed test cases for every CSS selector:
                           1. Identify all unique CSS selectors on the website.
                           2. For each selector, create test cases covering:
                              - Element presence and visibility
                              - Element properties (size, color, text content)
                              - Interaction behaviors (click, hover, input)
                              - Responsiveness across different screen sizes
                              - Cross-browser compatibility (Chrome, Firefox, Safari, Edge)
                           3. Include edge cases such as dynamic content loading and AJAX interactions.
                           4. Prioritize test cases based on critical user journeys.
                           5. Document any assumptions or prerequisites for each test case.""",
            agent=agent,
            expected_output="""Comprehensive set of test cases for each Element Name, covering various scenarios 
                               and potential issues.""",
            output_file='outputs/test_case.txt',
        )
    
    def gherkin_feature_file_creation(self, agent):
        return Task(
            description=#"""Transform the Element Name test cases into clear, concise BDD-style Gherkin feature files. 
                           #Ensure each scenario is well-defined and follows BDD best practices.""",
                           """Transform the CSS selector test cases into clear, concise BDD-style Gherkin feature files:
                           1. Group related test cases into features.
                           2. Create a feature file for each group of related functionality.
                           3. Write scenarios using Given-When-Then syntax, ensuring they are:
                              - Clear and concise
                              - Focused on business value
                              - Written in domain-specific language
                           4. Include scenario outlines for data-driven tests.
                           5. Add tags for easy filtering and organization.
                           6. Ensure coverage of happy paths, edge cases, and error scenarios.
                           7. Review and refine language for clarity and consistency.""",
            agent=agent,
            expected_output="""A set of feature files, each containing:
                               - A clear feature description
                               - Multiple scenarios covering different aspects of the feature
                               - Proper use of Given-When-Then syntax
                               - Appropriate tags for organization
                               - Scenario outlines where applicable
                               - Comments explaining any complex scenarios""",
            output_file='outputs/feature_file.txt',
            
        )
    
    def python_automation_script_development(self, agent):
        return Task(
            description=#"""Develop Python web automation scripts based on the Gherkin feature files. 
                           #Utilize appropriate frameworks (e.g., Selenium, Playwright) and implement 
                           #robust error handling and reporting mechanisms.""",
                           """Develop Python web automation scripts based on the Gherkin feature files:
                           1. Set up a Python project with necessary dependencies (Selenium, Pytest-BDD).
                           2. Create a robust Page Object Model (POM) structure.
                           3. Implement step definitions for each Gherkin step.
                           4. Develop utility functions for common operations (waits, JS execution).
                           5. Implement proper exception handling and logging.
                           6. Create custom commands for complex interactions.
                           7. Implement parameterization for data-driven tests.
                           8. Set up test data management (e.g., using fixtures or external files).
                           9. Implement hooks for setup and teardown operations.
                           10. Add screenshots and HTML reports for failed tests.""",
            agent=agent,
            expected_output="""Functional Python automation scripts that execute the scenarios defined 
                               in the Gherkin feature files, with proper assertions and error handling.""",
            output_file='outputs/automation_script.py',
        )
    
    def qa_review_and_integration(self, agent):
        return Task(
            description="""Review and ensure the quality and consistency of all outputs: Element Name test cases, 
                           Gherkin feature files, and Python automation scripts. Provide feedback for improvements 
                           and ensure alignment with QA best practices.""",
            agent=agent,
            expected_output="""Comprehensive review report highlighting strengths, areas for improvement, 
                               and suggestions for better integration of all components in the automation process.""",
        )
    
    