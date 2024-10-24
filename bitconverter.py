""" e) Converter de Imagem “Entrada.pgm” (8 bits escala de cinza, 0-255) em 5 bits de intensidade.
Obs. Lembre que 8 bits quer dizer que os valores variam de 0 a 255,
e 5 bits os valores variam de 0 a 31, o seja precisa ser desenvolvido um fator de conversão. """

def readImage(filepath):
    with open(filepath, "r") as image:
        imageType = image.readline().strip()
        assert imageType == "P2", "Não é P2"
        
        line = image.readline().strip()
        
        width, height = map(int, line.split())
        grayscaleBits = int(image.readline().strip())
        
        pixels = []
        for _ in range(height):
            row = []
            for _ in range(width):
                row.append(image.readline().strip())
            pixels.append(row)
        
    return pixels, width, height

def convertBits(pixels, oldRange, newRange, width, height):
    convertedPixels = []
    for y in range(height):
        newRow = []
        for x in range(width):
            chosenPixel = pixels[y][x]
            #convert
            newValue = ((int(chosenPixel) * newRange) // oldRange)
            newRow.append(newValue)
        convertedPixels.append(newRow)
    
    return convertedPixels


def saveIMG(filename, pixels, width, height, newRange):
    with open(filename, "w") as newImage:
        newImage.write("P2\n")
        newImage.write(str(width) + " " + str(height) + "\n")
        newImage.write(str(newRange) + "\n")
        
        for row in pixels:
            newImage.write(" ".join(map(str, row)) + "\n")
            
            
originalIMG = "Entrada_EscalaCinza.pgm"

pixels, width, height = readImage(originalIMG)
oldRange = 255
newRange = 31
convertedPixels = convertBits(pixels, oldRange, newRange, width, height)

output = "newIMG720p.pgm"
saveIMG(output, convertedPixels, width, height, newRange)