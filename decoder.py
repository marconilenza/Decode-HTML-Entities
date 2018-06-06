# -*- coding: utf-8 -*-

import sys

html_char = {
	'–' : '&ndash;',
	'"' : '&quot;',
	"'" : "&apos;",
	'&' : '&amp;',
	'Á' : '&Aacute;',
	'<' : '&lt;',
	'>' : '&gt;',
	' ' : '&nbsp;',
	'¡' : '&iexcl;',
	'¢' : '&cent;',
	'£' : '&pound;',
	'¤' : '&curren;',
	'¥' : '&yen;',
	'¦' : '&brvbar;',
	'§' : '&sect;',
	'¨' : '&uml;',
	'©' : '&copy;',
	'ª' : '&ordf;',
	'«' : '&laquo;',
	'¬' : '&not;',
	'®' : '&reg;',
	'¯' : '&macr;',
	'°' : '&deg;',
	'±' : '&plusmn;',
	'²' : '&sup2;',
	'³' : '&sup3;',
	'´' : '&acute;',
	'µ' : '&micro;',
	'¶' : '&para;',
	'·' : '&middot;',
	'¸' : '&cedil;',
	'¹' : '&sup1;',
	'º' : '&ordm;',
	'»' : '&raquo;',
	'¼' : '&frac14;',
	'½' : '&frac12;',
	'¾' : '&frac34;',
	'¿' : '&iquest;',
	'×' : '&times;',
	'÷' : '&divide;',
	'À' : '&Agrave;',
	'Á' : '&Aacute;',
	'Â' : '&Acirc;',
	'Ã' : '&Atilde;',
	'Ä' : '&Auml;',
	'Å' : '&Aring;',
	'Æ' : '&AElig;',
	'Ç' : '&Ccedil;',
	'È' : '&Egrave;',
	'É' : '&Eacute;',
	'Ê' : '&Ecirc;',
	'Ë' : '&Euml;',
	'Ì' : '&Igrave;',
	'Í' : '&Iacute;',
	'Î' : '&Icirc;',
	'Ï' : '&Iuml;',
	'Ð' : '&ETH;',
	'Ñ' : '&Ntilde;',
	'Ò' : '&Ograve;',
	'Ó' : '&Oacute;',
	'Ô' : '&Ocirc;',
	'Õ' : '&Otilde;',
	'Ö' : '&Ouml;',
	'Ø' : '&Oslash;',
	'Ù' : '&Ugrave;',
	'Ú' : '&Uacute;',
	'Û' : '&Ucirc;',
	'Ü' : '&Uuml;',
	'Ý' : '&Yacute;',
	'Þ' : '&THORN;',
	'ß' : '&szlig;',
	'à' : '&agrave;',
	'á' : '&aacute;',
	'â' : '&acirc;',
	'ã' : '&atilde;',
	'ä' : '&auml;',
	'å' : '&aring;',
	'æ' : '&aelig;',
	'ç' : '&ccedil;',
	'è' : '&egrave;',
	'é' : '&eacute;',
	'ê' : '&ecirc;',
	'ë' : '&euml;',
	'ì' : '&igrave;',
	'í' : '&iacute;',
	'î' : '&icirc;',
	'ï' : '&iuml;',
	'ð' : '&eth;',
	'ñ' : '&ntilde;',
	'ò' : '&ograve;',
	'ó' : '&oacute;',
	'ô' : '&ocirc;',
	'õ' : '&otilde;',
	'ö' : '&ouml;',
	'ø' : '&oslash;',
	'ù' : '&ugrave;',
	'ú' : '&uacute;',
	'û' : '&ucirc;',
	'ü' : '&uuml;',
	'ý' : '&yacute;',
	'þ' : '&thorn;',
	'ÿ' : '&yuml;',
}

try:
	file = sys.argv[1]
except:
	print("\n[+] Usage: python3", sys.argv[0], "file.txt\n")
	exit(1)

def decoder(file):
	f = open(file, "r")
	line = f.read()
	for key, val in html_char.items():
		line = line.replace(val,key)
	f.close()
	f = open(file, "w")
	f.write(line)
	f.close()
	print("Success!")

decoder(file)
