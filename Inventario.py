import streamlit as st
import pandas as pd

st.set_page_config(page_title="Gestión de Inventario", layout="centered")

st.title("📦 Sistema de Gestión de Productos")

if "inventario" not in st.session_state:
    st.session_state.inventario = []

st.subheader("Agregar Nuevo Producto")

with st.form("form_producto"):
    nombre = st.text_input("Nombre del Producto")
    precio = st.number_input("Precio ($)", min_value=0.0, step=0.5)
    cantidad = st.number_input("Cantidad en Stock", min_value=1, step=1)

    guardar = st.form_submit_button("Guardar Producto")

if guardar:
    if nombre.strip() != "":
        producto = {
            "Producto": nombre,
            "Precio": precio,
            "Cantidad": cantidad,
            "Total": precio * cantidad
        }

        st.session_state.inventario.append(producto)
        st.success("Producto agregado correctamente.")
    else:
        st.error("Ingresa el nombre del producto.")

if st.session_state.inventario:
    st.divider()
    st.subheader("📋 Inventario Actual")

    df = pd.DataFrame(st.session_state.inventario)
    st.dataframe(df, use_container_width=True)

    col1, col2 = st.columns(2)

    col1.metric(
        "Productos Distintos",
        len(st.session_state.inventario)
    )

    col2.metric(
        "Valor Total",
        f"${df['Total'].sum():,.2f}"
    )

    st.divider()
    st.subheader("🗑️ Eliminar Producto")

    nombres = [producto["Producto"] for producto in st.session_state.inventario]

    producto = st.selectbox(
        "Selecciona un producto:",
        nombres
    )

    if st.button("Eliminar Producto"):
        for item in st.session_state.inventario:
            if item["Producto"] == producto:
                st.session_state.inventario.remove(item)
                break

        st.success("Producto eliminado correctamente.")
        st.rerun()
else:
    st.info("No hay productos en el inventario.")
```
