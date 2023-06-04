"""Aquí hay un ejemplo que muestra cómo se verían 
   los docstrings según las recomendaciones de PEP 257. 
"""


def mi_funcion(parametro1, parametro2):
    """Breve descripción de la función.

    Descripción más detallada de la función y su funcionalidad.

    Args:
        parametro1: Descripción del primer parámetro.
        parametro2: Descripción del segundo parámetro.

    Returns:
        Valor de retorno: Descripción del valor de retorno (si corresponde).
    """
    # Cuerpo de la función
    pass

def calculate_area(length, width):
    """Calculate the area of a rectangle.

    Description 
    
    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The area of the rectangle.

    Raises:
        ValueError: If either length or width is negative.
    """
    if length < 0 or width < 0:
        raise ValueError("Length and width must be positive.")
    return length * width


class MiClase:
    """Breve descripción de la clase.

    Descripción más detallada de la clase y su funcionalidad.
    """

    def __init__(self, parametro1, parametro2):
        """Inicializador de la clase.

        Args:
            parametro1: Descripción del primer parámetro.
            parametro2: Descripción del segundo parámetro.
        """
        # Cuerpo del inicializador

    def mi_metodo(self):
        """Breve descripción del método.

        Descripción más detallada del método y su funcionalidad.

        Returns:
            Valor de retorno: Descripción del valor de retorno (si corresponde).
        """
        # Cuerpo del método
        pass
