import sublime_plugin

def mul(text, times):
	result = ""
	if times <= 0:
		return result
	for i in range(0, times):
		result += text
	return result


class ConvertToSuddenDeathCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		view = self.view
		for sel in view.sel():
			region = sel if sel else view.word(sel)
			word = view.substr(region)
			word_width = 0
			for c in list(word):
				word_width += (1 if len(str.encode(c)) == 1 else 2)
			dead_word = "\n＿" + mul("人", int((word_width+1)/2) + 2) + "＿\n" + \
									"＞　" + word + "　" + mul(" ", int(word_width%2)) + "＜\n" + \
									"￣" + mul("Ｙ", int((word_width+1)/2) + 2) + "￣\n"
			view.replace(edit, region, dead_word)


