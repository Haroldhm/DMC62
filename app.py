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
  # Inicializar la lista vacía en la sesión de Streamlit para no perder los datos
  if "movimientos" not in st.session_state:
      st.session_state.movimientos = []
  
  # --- DESCRIPCIÓN CON ST.MARKDOWN() ---
  st.markdown("""
  # Registro de Movimientos Financieros
  En este módulo podrás registrar tus ingresos y gastos de manera rápida. 
  Ingresa el concepto, selecciona el tipo de movimiento y coloca el valor. 
  Al presionar el botón, el registro se agregará a la lista y se calculará el flujo de caja final.
  """)
  
  # --- WIDGETS PARA INGRESAR DATOS ---
  concepto = st.text_input("Ingresa el concepto:")
  tipo = st.selectbox("Selecciona el tipo de movimiento:", ["Ingreso", "Gasto"])
  valor = st.number_input("Ingresa el valor:", min_value=0.0)
  
  # --- BOTÓN PARA AGREGAR MOVIMIENTOS ---
  if st.button("Agregar movimiento"):
      # Se agrega el movimiento como un diccionario a la lista
      st.session_state.movimientos.append(
          {"concepto": concepto, "tipo": tipo, "valor": valor}
      )
  
  # --- MOSTRAR LISTA DE MOVIMIENTOS ---
  st.subheader("Lista de movimientos registrados:")
  st.dataframe(st.session_state.movimientos)
  
  # --- CÁLCULO DE TOTALES Y SALDO FINAL ---
  total_ingresos = 0.0
  total_gastos = 0.0
  
  for movimiento in st.session_state.movimientos:
      if movimiento["tipo"] == "Ingreso":
          total_ingresos += movimiento["valor"]
      else:
          total_gastos += movimiento["valor"]
  
  saldo_final = total_ingresos - total_gastos
  
  # --- RESULTADOS Y MÉTRICAS ---
  st.metric("Total Ingresos", total_ingresos)
  st.metric("Total Gastos", total_gastos)
  st.metric("Saldo Final", saldo_final)
  
  # --- INDICADOR DEL FLUJO DE CAJA ---
  if saldo_final >= 0:
      st.success("El flujo de caja está: A FAVOR")
  else:
      st.error("El flujo de caja está: EN CONTRA") 

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
  
