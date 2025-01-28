import streamlit as st
from PIL import Image

# Configure the Streamlit app
st.set_page_config(
    page_title="Q.S Fashion - Men's Wear",
    page_icon="🎒",
    layout="wide"
)

# Sidebar Navigation
st.sidebar.title("Navigation")
menu = ["Home", "Products", "About Us", "Contact"]
choice = st.sidebar.radio("Go to:", menu)

# Home Section
if choice == "Home":
    st.title("Welcome to Q.S Fashion! 👔")
    #st.image("https://via.placeholder.com/1200x400?text=Q.S+Fashion+Men's+Wear", caption="Style That Defines You.")
    st.write("""
    **Q.S Fashion** offers premium men's wear for every occasion. Explore our latest collections, 
    enjoy seamless online shopping, and step into style today!
    
    ---
    """)
    st.subheader("Our Highlights:")
    st.write("""
    - Stylish and trendy men's apparel.
    - Affordable prices with premium quality.
    - Fast and reliable delivery across regions.
    - Exceptional customer support.
    """)

# Products Section
elif choice == "Products":
    st.header("Our Products 💼")

    products = [
        {"name": "Casual Shirts", "price": "$25", "image": "https://via.placeholder.com/300?text=Casual+Shirt"},
        {"name": "Formal Shirts", "price": "$30", "image": "https://via.placeholder.com/300?text=Formal+Shirt"},
        {"name": "T-Shirts", "price": "$20", "image": "https://via.placeholder.com/300?text=T-Shirt"},
        {"name": "Jeans", "price": "$40", "image": "https://via.placeholder.com/300?text=Jeans"},
        {"name": "Jackets", "price": "$60", "image": "https://via.placeholder.com/300?text=Jacket"},
        {"name": "Blazers", "price": "$100", "image": "https://via.placeholder.com/300?text=Blazer"},
    ]

    cols = st.columns(3)
    for idx, product in enumerate(products):
        with cols[idx % 3]:
            st.image(product["image"], use_column_width=True)
            st.subheader(product["name"])
            st.write(f"Price: {product['price']}")
            if st.button(f"Buy Now - {product['name']}", key=idx):
                st.success(f"Thank you for showing interest in {product['name']}! Our team will contact you soon.")

# About Us Section
elif choice == "About Us":
    st.header("About Q.S Fashion 🎓")
    st.write("""
    **Q.S Fashion** is a dedicated men's fashion store that focuses on bringing the latest trends to your doorstep. 
    We believe in combining style with comfort to give you the perfect wardrobe for every occasion. From casual outings to formal events, we have it all!

    **Our Mission:** To redefine men's fashion with high-quality, affordable, and trendy apparel.

    **Why Choose Us?**
    - Exclusive men's fashion collections.
    - Easy online shopping experience.
    - Unmatched quality at unbeatable prices.
    - Customer satisfaction is our top priority.

    Join the **Q.S Fashion family** today and elevate your style!
    """)

# Contact Section
elif choice == "Contact":
    st.header("Contact Us 📧")
    st.write("""
    We're here to help! Reach out to us for any inquiries, support, or feedback.

    ---

    **Email:** [contact@qsfashion.com](mailto:contact@qsfashion.com)
    
    **Phone:** +91-8051315478

    **Address:** Q.S Fashion, MUSLIM ROAD,NAWADA,BIHAR,INDIA

    **Social Media:**
    - [Instagram](https://instagram.com/qsfashion)
    - [Facebook](https://facebook.com/qsfashion)
    - [Twitter](https://twitter.com/qsfashion)
    """)

# Footer
st.sidebar.write("---")
st.sidebar.write("Made with ❤️ by Q.S Fashion Team (MD ANIQUE ZZAMA)")
