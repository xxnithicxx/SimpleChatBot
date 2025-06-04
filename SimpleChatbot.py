import streamlit as st

# Hàm respond_to_user trả về chuỗi
def respond_to_user(user_input: str) -> str:
    ui = user_input.lower().strip()

    # Chào người dùng
    if ui == "hi":
        return (
            "Xin chào quý khách! Tôi có thể giúp gì cho quý khách? ['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
        )
    elif ui == "hello":
        return (
            "Xin chào, bạn cần tôi giúp gì không? ['Tư vấn mua hàng', 'Tra cứu bảo hành', 'Hỗ trợ kỹ thuật']"
        )

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

# Danh sách các lệnh
COMMAND_BUTTONS = [
    "Hi",
    "Hello",
    "Tư vấn mua hàng",
    "Điện thoại",
    "Laptop",
    "Máy tính bảng",
    "Tra cứu bảo hành",
    "Tra cứu bằng số điện thoại",
    "Tra cứu bằng IMEI",
    "Hỗ trợ kỹ thuật",
    "Lỗi phần cứng",
    "Lỗi phần mềm",
]

# Thiết lập cấu hình Streamlit
st.set_page_config(
    page_title="Chatbot Hỗ Trợ Khách Hàng",
    layout="wide",
    initial_sidebar_state="auto"
)

# Khởi tạo session_state
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# Tiêu đề
st.title("Chatbot Hỗ Trợ Khách Hàng")

# Bố cục: 2 cột
#   - cột trái chứa các nút bấm sẵn
#   - cột phải hiển thị lịch sử trò chuyện
col_buttons, col_chat = st.columns([1, 3])

# 1) Cột trái
with col_buttons:
    st.markdown("### Danh sách lệnh sẵn:")
    for cmd in COMMAND_BUTTONS:
        if st.button(cmd, key=f"btn_{cmd}"):
            # Lưu tin nhắn của người dùng
            st.session_state["chat_history"].append({"sender": "user", "message": cmd})
            # Lấy phản hồi của Bot (trả về chuỗi)
            bot_reply = respond_to_user(cmd)
            st.session_state["chat_history"].append({"sender": "assistant", "message": bot_reply})

# 2) Cột phải
with col_chat:
    st.markdown("### Lịch sử trò chuyện:")
    for chat_item in st.session_state["chat_history"]:
        if chat_item["sender"] == "user":
            st.chat_message("user").write(chat_item["message"])
        else:
            st.chat_message("assistant").write(chat_item["message"])
