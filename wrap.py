class Wrap:
    def _handle_splitting_words(self, current, rest):
        if rest[0] != " ":
            last_position_of_space = current.rfind(" ")
            if last_position_of_space > 0:
                rest = current[last_position_of_space:] + rest
                current = current[:last_position_of_space]
        return current, rest

    def _format_rest_text(self, maxCharsPerLine, rest):
        return "\n" + self.text(rest.strip(), maxCharsPerLine)

    def _add_text_to_result(self, current_text, rest_text, max_columns):
        result = ""
        if len(rest_text) > 0:
            current_text, rest_text = self._handle_splitting_words(current_text, rest_text)
            result += current_text
            result += self._format_rest_text(max_columns, rest_text)
        else:
            result += current_text

        return result

    def text(self, text, max_columns):

        if max_columns >= len(text):
            return text

        current_text, rest_text = text[:max_columns], text[max_columns:]
        result = self._add_text_to_result(current_text, rest_text, max_columns)

        return result

wrap = Wrap()

print wrap.text("word", 6) == "word"
print wrap.text("wordword", 4) == "word\nword"
print wrap.text("wordword word", 4) == "word\nword\nword"
print wrap.text("wordword word", 4) == "word\nword\nword"
print wrap.text("wordword wordword", 4) == "word\nword\nword\nword"
print wrap.text("wordwordwordword", 4) == "word\nword\nword\nword"
print wrap.text("wordword wordword", 12) == "wordword\nwordword"
print wrap.text("tommyerkul", 5) == "tommy\nerkul"
print wrap.text("dette er en ganske lang tekst som skal deles opp i flere linjer ja",
          6) == "dette\ner en\nganske\nlang\ntekst\nsom\nskal\ndeles\nopp i\nflere\nlinjer\nja"
print wrap.text("litt vanskeligere tekst med noen lange ord", 6) == "litt\nvanske\nligere\ntekst\nmed\nnoen\nlange\nord"
print wrap.text("jeg synes dette var ganske artig", 15) == "jeg synes dette\nvar ganske\nartig"