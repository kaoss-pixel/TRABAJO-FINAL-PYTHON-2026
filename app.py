#IMPORTACIONES DE LIBROS
import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

#Creación Del Sidebar
st.sidebar.image("header.jpg")
opcion=st.sidebar.selectbox("Seleccione a donde se quiere dirigir:",["Home","Carga de data","ítem 1","ítem 2","ítem 3","ítem 4","ítem 5","ítem 6","ítem 7","ítem 8","ítem 9","ítem 10"])


if opcion=="Home":

    #Módulo 1: Home
    st.image("telcom.jpg")
    st.title("Home")
    st.markdown("**Análisis Exploratorio de Datos de Telco Consumer**")
    st.markdown("**Objetivo:**")
    st.write("El objetivo del proyecto del caso 2 es desarrollar un aplicativo " \
    "interactivo con python que permita realizar un ánalisis exploratorio completa" \
    " con la base de datos que nos otorga Teclco Customer, aplicando los conceptos aprendidos durantes la especialización. ")
    st.markdown("**Información del proyecto:**")
    st.write("**Nombre:** Kaori Romina Sakaguchi Santana")
    st.write("**Curso:** Especialización en Python para Análisis")
    st.write("**Año:**  2026")
    st.markdown("**Explicación de la dataset:**")
    st.write("El dataset presentada para el proyecto contiene información detallada de los clientes de telcom Customer Churn. " \
    "En esta data se puede ver los datos demográficos, el tipo de contrato que tiene, el método de pago, el total de cargo, emtre otros datos." \
    " La variable importante para este ánalisis es si el cliente sigue activo o no con los servicios de Telcom , con esta información podríamos analizar patrones de los clientes que han desactivado el servicio")
    st.markdown("**Tecnologías utilizadas:**")
    st.write("Python, Pandas, Streamlit, Matplotlib y Numpy")

#MODULO 2: CARGA DEL DATASET
#Utilizar st.file_uploader() para cargar el archivo .csv
#Validar que el archivo fue cargado correctamente
#Mostrar una vista previa del dataset (head)
#Mostrar dimensiones del dataset (filas y columnas)

elif opcion=="Carga de data":
    st.title("Carga de la data")
    st.markdown("Sube el archivo para comenzar el análisis")
    archivo=st.file_uploader("Selecciona el archivo", type=["csv","xlsx","txt"])
    if archivo is not None:
        nombre_archivo=archivo.name
        if nombre_archivo.endswith(".csv"):
            df=pd.read_csv(archivo)
        elif nombre_archivo.endswith(".xlsx"):
            df=pd.read_excel(archivo)
        elif nombre_archivo.endswith(".txt"):
            df=pd.read_csv(archivo)
        else:
            st.error("Fomarto no válido")
        
        st.session_state["df"]=df
        st.success("Archivo cargado correctoamente")
        st.write("Vista previa")
        st.dataframe(df.head())
        st.write("Dimensiones del dataset")
        st.write("Número de filas:", df.shape[0])
        st.write("Número de columnas:", df.shape[1])
    else:
        st.warning("Debe cargar el archivo para continuar")


#ITEM 1: INFORMACIÓN DE LA BASE DE DATOS
#info()
#Tipos de datos
#Conteo de valores nulos
elif opcion=="ítem 1":
    st.title("Información de la base de datos")
    st.write("En esta sección analizaremos sobre la estructura de la base de dato que se ha cargado")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        st.markdown("Información general de la base de datos")
        df.info()
        st.markdown("Tipo de datos")
        cuadro1=df.dtypes.reset_index()
        cuadro1.columns=["Variable","Tipo de dato"]
        st.dataframe(cuadro1)
        st.markdown("Valores nulos")
        cuadro2=df.isnull().sum().reset_index()
        cuadro2.columns=["Variable","Cantidad de nulos"]
        st.dataframe(cuadro2)
        st.markdown("Dimensiones de la base de datos")
        dimensiones={"Tipo":["Número de filas","Número de columnas"], "Cantidad":[df.shape[0],df.shape[1]]}
        dimension=pd.DataFrame(dimensiones)
        st.dataframe(dimension)


#ITEM 2: Clasificación de variables
#Identificación de variables: (Numericas y categoricas)
#Uso de una función personalizada
#Mostrar resultados con conteo
elif opcion=="ítem 2":
    st.title("Clasificación de variables")
    st.write("En esta sección identificaremos y clasificaremos cada una de las variables de la base de datos")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        def clasificacion_variables(df):
            numericas=df.select_dtypes(include="number").columns
            categoricas=df.select_dtypes(exclude="number").columns
            return numericas,categoricas
        numericas,categoricas=clasificacion_variables(df)    
        st.markdown("Variables Númericas")
        variable1=pd.DataFrame(numericas,columns=["Detalle"])
        st.dataframe(variable1)
        st.markdown("Variables Categoricas")
        variable2=pd.DataFrame(categoricas,columns=["Detalle"])
        st.dataframe(variable2)


#Ítem 3: Estadísticas descriptivas
#Uso de .describe()
#Interpretación básica de medias, medianas y dispersión
elif opcion=="ítem 3":
    st.title("Estadisticas Descriptivas")
    st.write("En esta sección podremos analizar las principales funciones estadisticas de las variables de la base de datos.")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        st.write("El resumen estadistico es:")
        numericas=df.select_dtypes(include="number")
        st.dataframe(numericas.describe())
        media=numericas.mean().reset_index()
        media.columns=["Variable","Media"]
        media["Media"]=media["Media"].round(2)
        mediana=numericas.median().reset_index()
        mediana.columns=["Variable","Mediana"]
        mediana["Mediana"]=mediana["Mediana"].round(2)
        desviacion=numericas.std().reset_index()
        desviacion.columns=["Variable","Desviación estándar"]
        desviacion["Desviación estándar"]=desviacion["Desviación estándar"].round(2)
        col1,col2,col3=st.columns(3)
        with col1:
            st.write("Media")
            st.dataframe(media)
        with col2:
            st.write("Mediana")
            st.dataframe(mediana)
        with col3:
            st.write("Desviación estándar")
            st.dataframe(desviacion)

        st.markdown("Interpretación de la información estadistica")
        #VALORES POR SEPARADO
        media_TotalCharges=round(numericas["TotalCharges"].mean(),2)
        media_tenure=round(numericas["tenure"].mean(),2)
        media_MonthlyCharges=round(numericas["MonthlyCharges"].mean(),2)
        mediana_TotalCharges=round(numericas["TotalCharges"].median(),2)
        mediana_tenure=round(numericas["tenure"].median(),2)
        mediana_MonthlyCharges=round(numericas["MonthlyCharges"].median(),2)
        desviacion_TotalCharges=round(numericas["TotalCharges"].std(),2)
        desviacion_tenure=round(numericas["tenure"].std(),2)
        desviacion_MonthlyCharges=round(numericas["MonthlyCharges"].std(),2)


        #INTERPRETACIÓN DE CADA UNO DE LOS FACTORES ESTADISTICOS
        st.write("")
        st.write("Interpretación de permanencia de los clientes:")
        st.write("1) El promedio de permanencia de los clientes es de:",media_tenure,"meses, sin embargo la mediana de los clientes es de:",mediana_tenure," Lo cual nos lleva a considerar que tenemos clientes que permanecen por un buen tiempo que elevan nuestro promedio de permanencia.")
        st.write("2) La desviación estandar es de",desviacion_tenure,"meses, lo que podría concluir que hay una alta variabilidad en los tiempos de permanencia.")
        st.write("Interpretación de los cargos mensuales:")
        st.write("1) El promedio de las cargas mensuales es de:",media_MonthlyCharges,"pesos, y sus mediana es de:", mediana_MonthlyCharges,"pesos. Podriamos concluir que hay grandes cargos mensuales que hace que nuestro promedio aumente.")
        st.write("2) La desviación estandar es de:",desviacion_MonthlyCharges,"pesos, lo que nos podría llevar a concluir que hay una alta variabilidad en los cargos mensuales.")


#item 4: Análisis de valores faltantes 
#Conteo 
#Visualización simple (si aplica) 
#Discusión breve
elif opcion=="ítem 4":
    st.title("Análisis de valores faltantes")
    st.write("En esta sección podremos analizar la presencia de valores vacios/nulos en la base de datos cargada.")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        nulos=df.isnull().sum().reset_index()
        nulos.columns=["Variable","Cantidad de valores nulos"]
        st.markdown("Cantida de valores faltantes")
        st.dataframe(nulos)
        nulos2=nulos[nulos["Cantidad de valores nulos"]>0]
        if len(nulos2)>0:
            st.markdown("Gráfico de los valores faltantes")
            plt.figure(figsize=(10,5))
            data=plt.bar(nulos2["Variable"],nulos2["Cantidad de valores nulos"])
            plt.title("Valores Faltantes")
            plt.bar_label(data)
            st.pyplot(plt)      
        else:
            st.write("No se encuentra ningun valor faltante en la base de datos")


#Ítem 5: Distribución de variables numéricas
#Histogramas
#Uso de Matplotlib o Seaborn
#Interpretación visual
elif opcion=="ítem 5":
    st.title("Distribución de variables numéricas")
    st.write("En esta sección podremos analizar la distribución de variables numéricas en la base de datos cargada. Con un gráfico incluido")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        #Gráfico
        numericas=df.select_dtypes(include="number")
        varnum=st.slider("Selecccione el número de intervalos de los gráficos",2,100,10)
        for column in numericas.columns:
            st.write("Distribución de", column)
            plt.figure()
            plt.hist(numericas[column],bins=varnum)
            plt.xlabel(column)
            plt.ylabel("Frecuencia")
            st.pyplot(plt)
            if column=="tenure":
                st.write("En el gráfico podemos observar el tiempo de permanencia de los clientes, si la mayoría se concentra en valores bajos indica que hay muchos clientes que tienen poca antiguedad.")
            elif column=="MonthlyCharges":
                st.write("En este gráfico de los cargos mensuales podemos, aqui podemos observar que si hay varios grupos esto indicaría que existen distintos planes con precio diferentes.")
            else:
                st.write("En este gráfico de los cargos total refleja el gasto acumulado de los clientes de telcom.")
#Ítem 6: Análisis de variables categóricas 
#Conteos 
#Gráficos de barras 
#Proporciones
elif opcion=="ítem 6":
    st.title("Análisis de variables categóricas")
    st.write("En esta sección podremos analizar la distribución de variables numéricas en la base de datos cargada. Con un gráfico incluido")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        categoricas=df.select_dtypes(exclude="number")
        for column in categoricas.columns:
            st.write("Detalle de ",column)   
            Q=df[column].value_counts()
            proporcion=df[column].value_counts(normalize=True)*100
            tablas=pd.DataFrame({"Categoría":Q.index,"Cantidad":Q.values,"Proporción":proporcion.values.round(2)})
            st.dataframe(tablas)
            #Gráfico
            plt.figure()
            Q.plot(kind="bar")
            plt.xlabel(column)
            plt.ylabel("Cantidad de clientes")
            plt.title("Distribución de "+column)
            st.pyplot(plt)
#ítem 7: Análisis bivariado (numérico vs categórico) 
#Ejemplos: MonthlyCharges vs Churn tenure vs Churn


elif opcion=="ítem 7":
    st.title("Análisis bivariado")
    st.write("En esta sección analizaremos las relaciones de los datos númericos y las categoricas, para identificar patrones y/o insights ")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        #TOTALCHARGE VS CHURN
        st.markdown("1. Relación entre la cancelación de los servicios y los cargos totales")
        media_TotalCharges=df.groupby("Churn")["TotalCharges"].mean().round(2)
        st.dataframe(media_TotalCharges)
        st.write("El promedio de los cargos totales con la cancelación de servicio es:",media_TotalCharges["Yes"])
        st.write("Considerar que los Yes son los clientes que dieron de baja su servicio")
        plt.figure()
        media_TotalCharges.plot(kind="bar")
        plt.ylabel("Promedio de cargos totales")
        plt.title("Promedio de los cargos totales según la permanencia del servicio")
        st.pyplot(plt)
        #ADULTOS MAYORES VS CHURN
        st.markdown("Relación entre los adultos mayores y la permanencia con el servicio")
        Q=df[df["SeniorCitizen"]==1]["Churn"].value_counts()
        proporcion=df[df["SeniorCitizen"]==1]["Churn"].value_counts(normalize=True)*100
        proporcion=proporcion.round(2)
        st.write("El porcentaje de los clientes adultos mayores que han dejado el servicio de telcom es de:",proporcion[1])
        tabla1=pd.DataFrame({"Estado de servicio":Q.index,"Cantidad": Q.values,"Proporción":proporcion.values})
        st.dataframe(tabla1)
        #ADULTOS MAYORES VS Totalcharge
        st.markdown("Relación entre los adultos mayores y el total de cargos")
        totalsenior=df.groupby("SeniorCitizen")["TotalCharges"].mean().round(2)
        st.write("Promedio del total de cargos de los adultos mayores es:")
        st.dataframe(totalsenior)
        plt.figure()
        totalsenior.plot(kind="pie")
        plt.title("Promedio de los pagos totales de los clientes de los adultos mayores")
        st.pyplot(plt)


#Ítem 8: Análisis bivariado (categórico vs categórico)
#Ejemplos:
#Contract vs Churn
#InternetService vs Churn


elif opcion=="ítem 8":
    st.title("Análisis bivariado - Datos Categoricas")
    st.write("En esta sección analizaremos los datos categoricas, para identificar patrones y/o insights ")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        #SERVICIO DE INTERNET CON ADULTOS MAYORES
        st.markdown("Análisis del servicio de internet en los adultos mayores")
        internet_sc=df.groupby("InternetService")["SeniorCitizen"].value_counts().reset_index()
        internet_sc.columns=["Tipo de internet","Adulto Mayor","Cantidad"]
        st.dataframe(internet_sc)
        if st.checkbox("Mostrar proporción de los adultos mayores que tienen servicio de internet:"):
            propsenior=df.groupby("InternetService")["SeniorCitizen"].value_counts(normalize=True)*100
            propsenior=propsenior.round(2)
            st.dataframe(propsenior)
        plt.figure()
        for servicio in df["InternetService"].unique():
            data=df[df["InternetService"]==servicio]["SeniorCitizen"].value_counts()
            plt.bar([servicio+"-"+ str(x) for x in data.index],data.values)
        plt.xticks(rotation=45)
        plt.ylabel("Cantidad de clientes adultos mayores")
        plt.title("Cantidad de personas con internet diferenciando a los adultos mayores")
        st.pyplot(plt)
        #METODOS DE PAGOS DE LOS ADULTOS MAYORES
        st.markdown("Análisis del metodo pago de los adultos mayores")
        df_scpago=df[df["SeniorCitizen"]==1]
        paymentsc=df_scpago["PaymentMethod"].value_counts()
        st.write("Medio de pago de los adultos mayores")
        st.dataframe(paymentsc)
        if st.checkbox("Mostrar proporción de métodos de pago en adultos mayores"):
            proppago=df_scpago["PaymentMethod"].value_counts(normalize=True)*100
            proppago=proppago.round(2)
            st.dataframe(proppago)
        plt.figure()
        paymentsc.plot(kind="bar")
        plt.xticks(rotation=45)
        plt.ylabel("Cantidad de clientes")
        plt.title("Medio de pago de los adultos mayores")
        for i in range(len(paymentsc.values)):
            plt.text(i,paymentsc.values[i],paymentsc.values[i],ha="center") 
        st.pyplot(plt)
        #TIPO DE SERVICIO DE INTERNET Y METODO DE PAGO
        st.markdown("Análisis del metodo pago según el servicio de internet")
        internet_pay=df.groupby("InternetService")["PaymentMethod"].value_counts().reset_index()
        internet_pay.columns=["Servicio de Internet","Método de pago","Cantidad"]
        st.write("Metodo de pago del internet")
        st.dataframe(internet_pay)
        if st.checkbox("Mostrar proporción de método de pago en cada servicio de internet"):
            propint=df.groupby("InternetService")["PaymentMethod"].value_counts(normalize=True)*100
            propint=propint.round(2)
            st.dataframe(propint)
        for servicio in df["InternetService"].unique():
            st.write("Metodo de pago del servicio de internet",servicio)
            data2=df[df["InternetService"]==servicio]["PaymentMethod"].value_counts()
            plt.figure()
            datos=plt.bar(data2.index,data2.values)
            plt.xticks(rotation=45)
            plt.ylabel("Cantidad de clientes")
            plt.title("Metodo de pago en "+servicio)
            for i in range(len(data2.values)):
                plt.text(i,data2.values[i], data2.values[i],ha="center")
            st.pyplot(plt)



   #Ítem 9: Análisis basado en parámetros seleccionados 
   #Uso de selectbox, multiselect 
   #Análisis dinámico según columnas elegidas por el usuario     

elif opcion=="ítem 9":
    st.title("Análisis basado en parámetros")
    st.write("En esta sección veremos y analizaremos información según los parámetros seleccionados.")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        st.write("Seleccione una variable para analizar:")
        categoricas=list(df.select_dtypes(exclude="number").columns)
        numerica=list(df.select_dtypes(include="number").columns)
        variables=st.multiselect("Seleccione las variables",categoricas+numerica)
        for col in variables:
            st.write("Información de: ",col)
            plt.figure()
            plt.hist(df[col])
            plt.xlabel(col)
            plt.ylabel("Frecuencia")
            st.pyplot(plt)





#Ítem 10: Hallazgos clave
#Visualización resumen
#Insights principales derivados del EDA

else:
    st.title("Hallazgos Clave")
    st.write("En esta sección veremos los hallazgos claves de toda la información evaluada de telcom")
    if "df" not in st.session_state:
        st.warning("Cargar archivo en la sección de **Carga de datos**")
    else:
        df=st.session_state["df"]
        df["TotalCharges"] = pd.to_numeric(df["TotalCharges"], errors="coerce")
        df["SeniorCitizen"] = df["SeniorCitizen"].astype("object")
        tab1, tab2, tab3=st.tabs(["Resumen General","Insights","Conclusión Final"])
        with tab1:
            st.subheader("Distribución General de los clientes que dieron de baja su servicio")
            qbaja=df["Churn"].value_counts()
            plt.figure()
            grafica1=plt.bar(qbaja.index,qbaja.values)
            plt.ylabel("Cantidad de clientes")
            plt.title("Estado del servicio de los clientes")
            for i in range(len(qbaja.values)):
                plt.text(i,qbaja.values[i],qbaja.values[i],ha="center")
            st.pyplot(plt)
            st.write("En este gráfico vemos la cantidad de clientes que permanecen con los servicios de telcom y tambien, quienes dieron de baja su servicio")
            st.subheader("Permanencia de los clientes adultos mayores")
            senior=df[df["SeniorCitizen"]==1]
            permanencia=round(senior["tenure"].mean(),2)
            st.write("El promeedio de permanencia de los servicios de telcom en los clientes adultos mayores es: ",permanencia,"meses.")
            plt.figure()
            plt.hist(senior["tenure"])
            plt.xlabel("Tiempo en meses")
            plt.ylabel("Frecuencia")
            plt.title("Distribución de la permanencia en telcom de los adultos mayores")
            st.pyplot(plt)
        with tab2:
            st.subheader("Principales insights")
            st.write("Pudimos observar que los clientes que cuentan con menor tiempo de permanencia, presentan mayor probabilidad de cancelación")
            st.write("La mayoría de los pagos realizados por los clientes que cuentan con internet es por Electronic check y Mailed check")
            st.write("El medio de pago que la mayoría de los adultos mayores que cuentan con internet es por Electronic Check")
            st.write("El internet que contrata la mayoría de los adultos mayores es el de fibra optica")
            st.write("El total de los cargos de los adultos mayores es mayor al de los adultos")
        with tab3:
            st.subheader("Conclusión final")
            st.write("En el anáñisis exploratorio que hemos realizado nos hemos enfocado en evaluar porque existe una gran cantidad de clientes que dejan los servicios, las variables que más nos han ayudado a comprender esto son:los medios de pagos, los pagos mensuales, los clientes adultos mayores y los servicio que telcom ofrece.")
            st.write("Hay factores como los cargos mensuales y el tiempo de permanencia que muestran una relación entre más cargos mensuales menos tiempo de permanencia, como tambien el método de pago utilizado por los adultos mayores es por Electronic Check.")
            st.write("Un gran porcentaje de nuestros clientes cuentan con el servicio de telefonia, mientras que en el servicio de internet si bien la mayoría tiene hay una gran cantidad de clientes que no cuentan con ese servicio.")
            st.write("Otro factor importante es saber que los cargos totales de los adultos mayores es mayor a los adultos, lo que hace que no permanezcan tanto con el servicio.")
            st.write("Cada uno de estos factores comentados, pueden ayudar a crear o mejoras productos enfocado en los adultos mayores.")
            st.write("Muchos de los clientes no cuentan con servicios de streaming de peliculas y ni de televisión, aunque hay un porcentaje de ellos que no cuentan con internet.")


                

        








