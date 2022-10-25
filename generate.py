import xml.etree.ElementTree as ET
import cairosvg

def set_numbers(numbers='m976aa34'):
    nine_svg = 'generate_numbers/rus.svg'
    eight_svg = 'generate_numbers/ru.svg'
    numbers = numbers.lower()
    chars = {
        'а' : 'A',
        'в' : 'B',
        'е' : 'E',
        'к' : 'K',
        'м' : 'M',
        'н' : 'H',
        'о' : 'O',
        'р' : 'P',
        'с' : 'C',
        'т' : 'T',
        'у' : 'Y',
        'х' : 'X'
    }
    number = ''
    for char in numbers:
        try:
            number += chars[char]
        except:
            number += char
    if len(number) == 9:
        svg = open(nine_svg, 'r').read()
        tree = ET.fromstring(svg)
        for elem in tree.iter('{http://www.w3.org/2000/svg}text'):
            id = elem.attrib['id']
            if id.startswith('plate'):
                text = ''
                for c in id[5:]:
                    text += number[int(c)]
                elem.text = text
        code = ET.tostring(tree)
        with open('generate_numbers/output.png', 'wb') as fout:
            cairosvg.svg2png(bytestring=code,write_to=fout)
    else:
        svg = open(eight_svg, 'r').read()
        tree = ET.fromstring(svg)
        for elem in tree.iter('{http://www.w3.org/2000/svg}text'):
            id = elem.attrib['id']
            if id.startswith('plate'):
                text = ''
                for c in id[5:]:
                    text += number[int(c)]
                elem.text = text
        code = ET.tostring(tree)
        with open('generate_numbers/output.png', 'wb') as fout:
            cairosvg.svg2png(bytestring=code,write_to=fout)
    return open('generate_numbers/output.png', 'rb')