import streamlit as st
import pandas as pd
import joblib

st.title("🛒 Prediksi Total Penjualan Supermarket")

@st.cache_resource
def muat_model():
    return joblib.load("model_supermarket.joblib")

model = muat_model()

unit_price = st.slider("Harga Satuan Produk", 10.0, 100.0, 50.0, 0.1)
quantity = st.slider("Jumlah Produk", 1, 10, 5)
rating = st.slider("Rating Pelanggan", 4.0, 10.0, 7.0, 0.1)

branch = st.selectbox("Cabang", ["A", "B", "C"])
customer = st.selectbox("Jenis Pelanggan", ["Member", "Normal"])
product = st.selectbox("Kategori Produk", [
    "Health and beauty",
    "Electronic accessories",
    "Home and lifestyle",
    "Sports and travel",
    "Food and beverages",
    "Fashion accessories"
])
payment = st.selectbox("Metode Pembayaran", [
    "Cash", "Ewallet", "Credit card"
])

if st.button("🔮 Prediksi Total Penjualan"):
    data_baru = pd.DataFrame({
        "Unit price": [unit_price],
        "Quantity": [quantity],
        "Rating": [rating],
        "Branch": [branch],
        "Customer type": [customer],
        "Product line": [product],
        "Payment": [payment]
    })

    total = model.predict(data_baru)[0]

    st.success(f"Perkiraan Total Penjualan: {total:.2f}")
