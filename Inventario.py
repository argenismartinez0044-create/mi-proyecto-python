import streamlit as st
import pandas as pd

# Configuración de la página
st.set_page_config(page_title="Gestión de Inventario", layout="centered")

st.title("📦 Sistema de Gestión de Productos")

# Inicializar inventario en la sesión si no existe
if "inventario" not in st.session_state:
    st.session_state.inventario = []

# Formulario para agregar productos
with st.form("form_producto"):
    st.subheader("Agregar Nuevo Producto")
    nombre = st.text_input("Nombre del Producto")
    precio = st.number_input("Precio ($)", min_value=0.0, step=0.5)
    cantidad = st.number_input("Cantidad en Stock", min_value=1, step=1)
    
    btn_guardar = st.form_submit_button("Guardar Producto")

if btn_guardar:
    if nombre.strip() != "":
        nuevo_item = {"Producto": nombre, "Precio": precio, "Cantidad": cantidad, "Total": precio * cantidad}
        st.session_state.inventario.append(nuevo_item)
        st.success(f"¡{nombre} agregado correctamente!")
    else:
        st.error("Por favor, ingresa un nombre válido.")

# Mostrar tabla y métricas si hay datos
if st.session_state.inventario:
    st.divider()
    st.subheader("📋 Inventario Actual")
    
    df = pd.DataFrame(st.session_state.inventario)
    st.dataframe(df, use_container_width=True)
    
    # Métricas
    col1, col2 = st.columns(2)
    col1.metric("Total de Productos Distintos", len(df))
    col2.metric("Valor Total del Inventario", f"${df['Total'].sum():,.2f}")
