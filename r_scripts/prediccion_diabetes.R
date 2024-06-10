# Carga el modelo entrenado
load("r_scripts/models/modelo_diabetes.rda")

# Carga el paquete neuralnet
library(neuralnet)

# Define la función de predicción
predecir_diabetes <- function(edad, genero, peso, altura, glucosa_ayunas) {
  # Codificar la variable 'genero' utilizando one-hot encoding manual
  if (genero == "M") {
    F <- 0
    M <- 1
  } else if (genero == "F") {
    F <- 1
    M <- 0
  } else {
    stop("Genero no valido. Use 'M' para Masculino o 'F' para Femenino.")
  }
  
  # Crear un data.frame con los datos del formulario
  datos <- data.frame(
    edad = as.numeric(edad),
    F = F,
    M = M,
    peso = as.numeric(peso),
    altura = as.numeric(altura),
    glucemia = as.numeric(glucosa_ayunas)
  )
  
  # Realiza la predicción utilizando el modelo cargado
  predicciones <- compute(modelo_diabetes, datos)
  
  # Redondear el resultado para obtener una predicción binaria (0 o 1)
  prediccion_binaria <- ifelse(predicciones$net.result > 0.5, 1, 0)
  
  return(prediccion_binaria)
}

# Leer los argumentos de la línea de comandos
args <- commandArgs(trailingOnly = TRUE)

# Asegurarse de que se pasen todos los argumentos necesarios
if (length(args) != 5) {
  stop("Numero incorrecto de argumentos. Se necesitan 5 argumentos: edad, genero, peso, altura, glucosa_ayunas.")
}

# Realizar la predicción y mostrar el resultado
tryCatch({
  resultado <- predecir_diabetes(args[1], args[2], args[3], args[4], args[5])
  if (resultado == 1) {
    cat("Es posible que pueda tener diabetes en el futuro. Por favor, consulte a su médico.\n")
  } else {
    cat("Es poco probable que tenga diabetes en el futuro. Continúe con su estilo de vida saludable.\n")
  }
}, error = function(e) {
  cat("Error en la predicción:", e$message, "\n")
})
