f = open("webpage.html", "w")

f.write("<html>\n")
f.write("<body bgcolor='pink'>\n")

f.write("<h1>CPSC 111</h1>\n")
f.write("<ul><li>Gordon Simon</li><li>604-512-6200</li></ul>\n")

f.write("</body>\n")
f.write("</html>\n")
f.close()

print "HMTL program is written to file"
