import re
# for the first name :First character uppercase an the rest in lowercase
# for the second name: may have or haven't second name
# if have then is the same format that the first name
name_pattern = re.compile(r'[A-Z][a-z]{2,}\s?[A-Z]?[a-z]{0,}')

# is the same format that the name
lastname_pattern = re.compile(r'[A-Z][a-z]{2,}\s?[A-Z]?[a-z]{0,}')

# implementation of RFC 5332 taken from http://www.regular-expressions.info/email.html
# before the @
email_pattern = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*"
# after the @
r"@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")


address_pattern = re.compile(
# type of road
r"""^(AUTOPISTA|AVENIDA|AVENIDA CALLE|AVENIDA CARRERA|BULEVAR|CALLE|CARRERA|CARRETERA|CIRCUNVALAR|DIAGONAL|PASAJE|
PASEO|PEATONAL|TRANSVERSAL|TRONCAL|VARIANTE|VÍA|VIA|AU|AV|AC|AK|BL|CL|KR|CT|CQ|CV|CC|DG|PJ|PS|PT|TV|TC|VT|VI|IND)\s"""
# Main Nomenclature number + letter main nomenclature + bis if exist + quadrant

r"([A-Z]{2,})?\s?([0-9]{1,2})?[A-Z]?\s(BIS)?\s?[A-Z]?\s?(NORTE|SUR|ESTE|OESTE|N|S|E|O)?\s?(NO|NO.|N|#| ?)\s?([0-9]{1,2})?[A-Z]?(-| )?([0-9]{1,2})?\s?(NORTE|SUR|ESTE|OESTE|N|S|E|O)?"
# complement
r"""\s?(((ADMINISTRACION|AGRUPACION|ALTILLO|APARTAMENTO|BARRIO|BLOQUE|CASA|CELULA|CIUDADELA|CENTRO COMERCIAL|CONJUNTO RECIDENCIAL|
CONSULTORIO|DEPOSITO|EDIFICIO|ENTRADA|ESQUINA|ESTACION|ETAPA|FINCA|GARAJE|INTERIOR|KILOMETRO|LOCAL|LOTE|MANZANA|MEZZANINE|MODULO|OFICINA|
PARQUE|PISO|PLANTA|PORTERIA|PREDIO|PUESTO|SECTOR|SOTANO|TERRAZA|UNIDAD|URBANIZACION|ZONA|AD|AG|AL|AP|BR|BQ|CS|CU|CE|CD|CO|CN|DP|DS|ED|EN|
EQ|ES|ET|EX|FI|GA|GS|IN|KM|LC|LM|LT|MZ|MD|OF|PQ|PA|PN|PI|PL|PR|PD|PU|RP|SC|SS|SO|ST|SM|TZ|TO|UN|UL|UR|ZN)\s((([A-Z0-9-])+)\s?)?)+)?$"""
,re.IGNORECASE)


#DD-MM-AAAA
#DD.MM.AAAA
#DD/MM/AAA
birthday_pattern = re.compile(r"""(?:3[01]|[12][0-9]|0?[1-9])([\-/.])(0?[1-9]|1[1-2])\1\d{4}""")
#((3(0|1))|((1|2)[0-9])|0?[1-9])+(|\-|/|.)?((0?[1-9])|(1[1-2]))+(|\-|/|.)?

mobile_pattern = re.compile(r'3[0-9]{9}')
phone_pattern = re.compile(r'[0-9]{7}')
postal_code_pattern = re.compile(r"""(11|91|05|81|08|13|15|17|18|85|19|20|27|23|25|94|95|41|44|47|50|52|54|86|63|66|
88|68|70|73|76|97|99)+[0-9]{4}""")

#print(phone_pattern.match("a"))



def assess(form:dict)->str:
    """ asses data dictionary 

    Args:
        form (dict): dictionary with the form information

    Returns:
        str: Errors in the form
    """
    print(email_pattern.match(form['email']))

    output=""
    if name_pattern.match(form['name'])==None: output+="Error en el Nombre\n"
    if lastname_pattern.match(form['last_name'])==None: output+="Error en el Apellido\n"
    if address_pattern.match(form['address'])==None: output+="Error en la Dirección\n"
    if email_pattern.match(form['email'])==None: output+="Error en el Email\n"
    if birthday_pattern.match(form['birthday'])==None: output+="Error en la Fecha de Nacimiento\n"
    if mobile_pattern.match(form['mobile'])==None: output+="Error en el numero de Celular\n"
    if phone_pattern.match(form['phone'])==None: output+="Error en el numero Fijo\n"
    if postal_code_pattern.match(form['postal_code'])==None: output+="Error en el codigo postal\n"
    if output=="":output="Has llenado el formulario con exito"
    return output




