import streamlit as st

# Hàm trả lời người dùng
def respond_to_user(user_input: str) -> str:
    ui = user_input.lower().strip()

    # Chào người dùng
    if ui == "hi":
        return "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
    elif ui == "hello":
        return "['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"

    # Tư vấn mua hàng
    elif ui == "tư vấn mua hàng":
        return "['điện thoại', 'laptop', 'máy tính bảng']"
    elif ui == "điện thoại":
        return "Quý khách muốn mua điện thoại nào ạ?"
    elif ui == "laptop":
        return "Quý khách muốn mua laptop nào ạ?"
    elif ui == "máy tính bảng":
        return "Quý khách muốn mua tablet nào ạ?"

    # Tra cứu bảo hành
    elif ui == "tra cứu bảo hành":
        return "['tra cứu bằng số điện thoại', 'tra cứu bằng IMEI']"
    elif ui == "tra cứu bằng số điện thoại":
        return "Quý khách vui lòng nhập số điện thoại để tra cứu bảo hành"
    elif ui == "tra cứu bằng imei":
        return "Quý khách vui lòng nhập IMEI để tra cứu bảo hành"

    # Hỗ trợ kỹ thuật
    elif ui == "hỗ trợ kỹ thuật":
        return "['lỗi phần cứng', 'lỗi phần mềm']"
    elif ui == "lỗi phần cứng":
        return "Quý khách vui lòng mô tả lỗi phần cứng để được hỗ trợ"
    elif ui == "lỗi phần mềm":
        return "Quý khách vui lòng mô tả lỗi phần mềm để được hỗ trợ"

    # Không hiểu yêu cầu
    else:
        return "Xin lỗi! Tôi không hiểu yêu cầu của bạn. Bạn có thể nói rõ hơn không?"

# Thiết lập cấu hình Streamlit
st.set_page_config(
    page_title="Chatbot Hỗ Trợ Khách Hàng",
    layout="wide",
    initial_sidebar_state="auto"
)

# Sidebar
with st.sidebar:
    st.markdown("## Hướng dẫn sử dụng")
    st.write("- Gõ “Hi” hoặc “Hello” để bắt đầu.")
    st.write("- Nhập từ khoá theo gợi ý của chatbot (ví dụ: 'Tư vấn mua hàng', 'Điện thoại', …).")
    st.write("- Để xóa toàn bộ lịch sử, nhấn nút bên dưới.")
    if st.button("Xoá lịch sử"):
        st.session_state["chat_history"] = []

# Khởi tạo session_state cho lịch sử trò chuyện
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

st.title("Chatbot Hỗ Trợ Khách Hàng")

# Hiển thị toàn bộ lịch sử trò chuyện
for chat_item in st.session_state["chat_history"]:
    if chat_item["sender"] == "user":
        st.chat_message("user").write(chat_item["message"])
    else:
        st.chat_message("assistant").write(chat_item["message"])

# Ô nhập tin nhắn và xử lý đầu vào
if prompt := st.chat_input("Nhập tin nhắn của bạn..."):
    st.session_state["chat_history"].append({"sender": "user", "message": prompt})
    bot_reply = respond_to_user(prompt)
    st.session_state["chat_history"].append({"sender": "assistant", "message": bot_reply})
    st.chat_message("user").write(prompt)
    st.chat_message("assistant").write(bot_reply)