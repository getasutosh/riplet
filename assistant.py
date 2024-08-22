import streamlit as st
import openai

# Set your OpenAI API key
openai.api_key = "your_openai_api_key_here"

# Define the prompt template
def create_prompt(user_request):
    prompt = f"""
    You are an AI assistant for Rippling, a company that provides various products on its platform. Your task is to help users navigate to the appropriate app and landing page based on their requests, and suggest possible actions when applicable.

    First, here is the information about Rippling's products and their corresponding apps from rippling.com.

    When a user makes a request, follow these steps:

    1. Analyze the user's request carefully, identifying key words and intentions.
    2. Based on the request, determine which Rippling app and specific feature or landing page within that app would be most appropriate to address the user's needs.
    3. Provide clear navigation instructions to guide the user to the correct app and landing page.
    4. If possible, suggest any specific actions the user might take once they reach the appropriate page.
    5. If the user's request is unclear or doesn't seem to match any of Rippling's products, ask for clarification or provide general information about Rippling's offerings.

    Present your response in the following format:

    <response>
    <app>Name of the appropriate Rippling app</app>
    <navigation>Step-by-step instructions on how to navigate to the correct landing page</navigation>
    <suggested_actions>List of possible actions the user can take (if applicable)</suggested_actions>
    <additional_info>Any clarifications or extra information (if needed)</additional_info>
    </response>

    Remember to be helpful, clear, and concise in your responses. If you're unsure about any aspect of the request, it's better to ask for clarification than to provide incorrect information.

    <user_request>
    {user_request}
    </user_request>
    """
    return prompt

# Define the Streamlit app
def main():
    st.title("Rippling AI Assistant")
    
    # User input
    user_request = st.text_area("Enter your request", "")
    
    # Generate response when the button is clicked
    if st.button("Get Response"):
        if user_request:
            with st.spinner("Generating response..."):
                prompt = create_prompt(user_request)
                response = openai.Completion.create(
                    model="gpt-4",  # You can use "gpt-3.5-turbo" for faster response
                    prompt=prompt,
                    max_tokens=1000,
                    temperature=0,
                )
                st.markdown("### AI Assistant Response:")
                st.write(response.choices[0].text)
        else:
            st.warning("Please enter a request.")

if __name__ == "__main__":
    main()
