import streamlit as st
import numpy as np
import libreria_funciones as lf

##Elaboracion de sidebar
st.sidebar.title("Paginas")
st.sidebar.image("DMC.png",width =250)

##Creacion de tema/logo pagina
st.image("Logo_proyecto.png",width =2000)
st.write("Elaborado por: Harold Hernandez")

modulos = st.sidebar.selectbox("Selecione el módulo",["Home","Ejercicio1", "Ejercicio2", "Ejercicio3", "Ejercicio4"])

if modulos == "Home":

  st.subheader("APLICACIÓN EN STREAMLIT")
  st.markdown("**Nombre:** Harold Hernandez Medina")
  st.markdown("**Modulo:**  Python Fundamentals")
  st.markdown("**Edad:**  25 años")
  st.markdown("**Año:**  2026")
  st.markdown("**Descripcion:**  Una aplicación interactiva en Streamlit integrando los contenidos revisados en el módulo")
  st.markdown("**Tecnologias:**  GitHub,Streamlit,Python")


## valor_inicial = int(st.number_input("Ingresa tu valor inicial del rango", value=0))
## valor_final = int(st.number_input("Ingresa tu valor final del rango",value=10))

##  lista = list(range(valor_inicial, valor_final))

##  st.write(lista)


elif modulos == "Ejercicio1":
  st.subheader("EJERCICIO 1")
st.set_page_config(page_title="Control Financiero Simple", page_icon="💰")

# 1. Inicializar la lista vacía en la sesión de Streamlit
if "movimientos" not in st.session_state:
    st.session_state.movimientos = []

# 2. Descripción del ejercicio con st.markdown()
st.title("💰 Módulo de Movimientos Financieros")

st.markdown("""
Esta aplicación permite registrar **ingresos y gastos** de forma sencilla.
Ingresa los datos del movimiento y presiona el botón para guardarlo.
""")

st.divider()

# 3. Widgets para ingresar los datos
concepto = st.text_input("Concepto:", placeholder="Ej. Sueldo, Alquiler...")
tipo = st.selectbox("Tipo de movimiento:", ["Ingreso", "Gasto"])
valor = st.number_input("Valor ($):", min_value=0.0, step=1.0)

# 4. Botón para agregar movimientos a la lista
if st.button("➕ Agregar movimiento"):
    if concepto != "" and valor > 0:
        # Agregamos un diccionario con el movimiento a nuestra lista
        st.session_state.movimientos.append(
            {"concepto": concepto, "tipo": tipo, "valor": valor}
        )
        st.success("¡Movimiento registrado con éxito!")
    else:
        st.warning("Escribe un concepto y un valor mayor a cero.")

st.divider()

# 5. Mostrar la lista y realizar los cálculos
st.subheader("📋 Lista de movimientos")

if len(st.session_state.movimientos) == 0:
    st.info("No hay movimientos registrados aún.")
else:
    # Variables para calcular los totales
    total_ingresos = 0.0
    total_gastos = 0.0

    # Recorremos la lista para mostrarla y sumar
    for item in st.session_state.movimientos:
        st.write(f"• **{item['concepto']}** ({item['tipo']}): ${item['valor']:,.2f}")

        if item["tipo"] == "Ingreso":
            total_ingresos += item["valor"]
        else:
            total_gastos += item["valor"]

    saldo_final = total_ingresos - total_gastos

    st.divider()

    # 6. Muestra de métricas y resultado final
    st.subheader("📊 Resultados")

    col1, col2, col3 = st.columns(3)
    col1.metric("Total Ingresos", f"${total_ingresos:,.2f}")
    col2.metric("Total Gastos", f"${total_gastos:,.2f}")
    col3.metric("Saldo Final", f"${saldo_final:,.2f}")

    # Indicar si el flujo de caja está a favor o en contra
    if saldo_final >= 0:
        st.success(f"🟢 El flujo de caja está **A FAVOR**")
    else:
        st.error(f"🔴 El flujo de caja está **EN CONTRA**")

    # Botón para limpiar la lista
    if st.button("🗑️ Limpiar todo"):
        st.session_state.movimientos = []
        st.rerun()




 ## cantidad = st.slider("Seleccione un valor del rango", min_value = 1, max_value = 100, value=20 )
 ## arreglo = np.arange(cantidad)

 ## st.write(arreglo)

elif modulos == "Ejercicio2":
  st.write("Te encuentras en el módulo de arreglos")

elif modulos == "Ejercicio3":
  st.write("Te encuentras en el módulo de Funciones")
  capital_i = st.number_input("Ingrese el capital inicial", min_value = 0 , max_value = 100000, value=1000)
  aporte_m = st.number_input("Ingrese el aporte mensual", min_value = 0 , max_value = 10000, value=100)
  tasa_a = st.slider("Ingrese el aporte mensual", min_value = 0.01 , max_value = 1.00, value=0.05)
  anios = st.slider("Ingrese el aporte mensual", min_value = 1 , max_value = 20, value=2)

  resultado_valor_futuro = lf.valor_futuro_inversion(capital_i ,aporte_m,tasa_a,anios)
  st.write("El resultados de tu valor futuro de inversión es: ",round(resultado_valor_futuro,2))
  
else:
  st.write("Te encuentras en el módulo de Ejercicio4")
  
