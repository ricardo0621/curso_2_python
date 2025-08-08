import csv
import os
from typing import List, Dict, Any

def contar_lotes(ruta_archivo: str) -> Dict[str, int]:
    """
    Lee un archivo CSV y cuenta la cantidad de cada lote.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV a leer
        
    Returns:
        Dict[str, int]: Diccionario con el lote como clave y la cantidad como valor
    """
    try:
        # Verificar si el archivo existe
        if not os.path.exists(ruta_archivo):
            raise FileNotFoundError(f"El archivo '{ruta_archivo}' no existe")
        
        contador_lotes = {}
        total_filas = 0
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            # Crear un lector CSV
            lector_csv = csv.DictReader(archivo)
            
            # Verificar si existe el campo 'lote'
            if 'lote' not in lector_csv.fieldnames:
                print("❌ Error: No se encontró el campo 'lote' en el archivo CSV")
                print(f"Campos disponibles: {lector_csv.fieldnames}")
                return {}
            
            # Leer cada fila y contar los lotes
            for numero_fila, fila in enumerate(lector_csv, start=1):
                valor_lote = fila.get('lote', '').strip()
                if valor_lote:  # Solo contar si no está vacío
                    contador_lotes[valor_lote] = contador_lotes.get(valor_lote, 0) + 1
                total_filas += 1
        
        print(f"📊 Total de filas procesadas: {total_filas}")
        print(f"📊 Total de lotes únicos: {len(contador_lotes)}")
        return contador_lotes
        
    except FileNotFoundError as e:
        print(f"Error: {e}")
        return {}
    except Exception as e:
        print(f"Error al leer el archivo CSV: {e}")
        return {}

def mostrar_encabezados(ruta_archivo: str) -> List[str]:
    """
    Función simplificada que solo obtiene y muestra los encabezados del archivo CSV.
    
    Args:
        ruta_archivo (str): Ruta del archivo CSV
        
    Returns:
        List[str]: Lista de encabezados
    """
    try:
        if not os.path.exists(ruta_archivo):
            print(f"Error: El archivo '{ruta_archivo}' no existe")
            return []
        
        with open(ruta_archivo, 'r', encoding='utf-8') as archivo:
            lector_csv = csv.DictReader(archivo)
            encabezados = lector_csv.fieldnames
            
            if encabezados:
                print("Encabezados del archivo CSV:")
                for i, encabezado in enumerate(encabezados, 1):
                    print(f"{i}. {encabezado}")
            else:
                print("No se encontraron encabezados en el archivo CSV")
            
            return encabezados if encabezados else []
            
    except Exception as e:
        print(f"Error al leer los encabezados: {e}")
        return []

# Ejemplo de uso
if __name__ == "__main__":
    # Archivo CSV específico - ubicado en la carpeta data
    archivo_csv = "../../data/guias_4000_.csv"
    
    print("=== CONTEO DE LOTES DEL ARCHIVO GUIAS_4000_.CSV ===")
    print(f"Procesando archivo: {archivo_csv}")
    print("=" * 60)
    
    # Verificar si el archivo existe
    if os.path.exists(archivo_csv):
        print("✅ Archivo encontrado")
        
        # Contar lotes
        contador_lotes = contar_lotes(archivo_csv)
        
        if contador_lotes:
            print(f"\n📋 CONTEO DE LOTES:")
            print("-" * 40)
            
            # Ordenar por cantidad (de mayor a menor)
            lotes_ordenados = sorted(contador_lotes.items(), key=lambda x: x[1], reverse=True)
            
            for lote, cantidad in lotes_ordenados:
                print(f"   Lote: {lote:<15} | Cantidad: {cantidad:>5}")
            
            print("-" * 40)
        
    else:
        print(f"❌ Error: El archivo '{archivo_csv}' no existe")
        print(f"📁 Directorio actual: {os.getcwd()}")
        print(f"🔍 Buscando en: {os.path.abspath(archivo_csv)}")
        print("💡 Verifica que el archivo esté en la carpeta 'data' del proyecto")
    
