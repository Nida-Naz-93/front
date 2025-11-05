import streamlit as st
import requests
import json

# === CONFIGURATION ===
WEBHOOK_URL = "https://nida-naz06.app.n8n.cloud/webhook/b0f2c6f1-a32e-4c10-bd9e-f31127fb6910"  # Replace with your production webhook URL

# === UI DESIGN ===
st.set_page_config(page_title="Taxonify AI Chat", page_icon="💬", layout="centered")

st.title("💬 Taxonify AI Assistant")
st.write("Ask me anything about Taxonify!")

# === USER INPUT ===
user_message = st.text_input("Your Message:", placeholder="Type your question here...")

if st.button("Send"):
    if not user_message.strip():
        st.warning("Please enter a message before sending.")
    else:
        try:
            # === SEND TO N8N WEBHOOK ===
            payload = {"message": user_message}
            headers = {"Content-Type": "application/json"}

            response = requests.post(WEBHOOK_URL, headers=headers, data=json.dumps(payload))

            # === DISPLAY RESPONSE ===
            if response.status_code == 200:
                data = response.json()
                st.success("✅ AI Response:")
                st.write(data.get("reply", "No reply received. Check your workflow output."))
            else:
                st.error(f"⚠️ Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"❌ Request failed: {str(e)}")

st.markdown("---")
st.caption("Powered by n8n + GPT-4o + Streamlit")
