# read final.txt line by line and add to a list
def read_file():
    with open("final.txt", "r") as f:
        lines = f.readlines()
        return lines

# use every line to construct a js command
# i for time it takes to run the command
# pop lines everytime it is called
# command example
# document.evaluate("//div[normalize-space(text())='TEXT to substitute']", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();


def copyCommandToClipboard(i, lines):
    commands = []
    commands.append('let x = document.querySelectorAll("div.flex-fill")')
    commands.append("try {")
    for line in lines:
        while i > 0:
            line = lines.pop(0)
            # if ① or ② or ③ or ④ in line, change to console.warn
            if '①' in line or '②' in line or '③' in line or '④' in line:
                # command = "console.log('" + line.strip() + "');"
                command = 'Array.from(x).find((node) => node.innerText == "' + line.strip() + '\\n").click();'
            else:
                command = 'Array.from(x).find((node) => node.innerText == "' + line.strip() + '").click();'
            #     command = "document.evaluate(`//div[normalize-space(text())='" + line.strip(
            #     ) + "']`, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click();"
            commands.append(command)
            i -= 1
    commands.append("} catch (e) {}")
    pyperclip.copy('\n'.join(commands))
    print('\n'.join(commands))
    print("Copied to clipboard")
    print("------------------------------------------------------")

def saveRestLines(lines):
    with open("final.txt", "w") as f:
        f.writelines(lines)

if __name__ == "__main__":
    import pyperclip
    lines = read_file()
    i = int(input("How many questions are there: "))
    while i != -1:
        copyCommandToClipboard(i, lines)
        i = int(input("How many questions are there, -1 to exit: "))
    saveRestLines(lines)
