import re
from typing import NamedTuple, Iterable


class Token(NamedTuple):
    kind: str
    value: str


def lex(code: str) -> Iterable[Token]:
    """
    Retorna sequência de objetos do tipo token correspondendo à análise léxica
    da string de código fornecida.
    """

    tokens = [
        ("STRING", r"\".*\""),
        ("NUMBER", r"(\+|\-|)\d+(\.\d*)?"),
        ("NAME", r"([a-zA-Z_%\+\-]|\.\.\.)[a-zA-Z_0-9\-\>\?\!]*"),
        ("CHAR", r"#\\[a-zA-Z]*"),
        ("BOOL", r"#[t|f]"),
        ("QUOTE", r"\'"),
        ("LPAR", r"\("),
        ("RPAR", r"\)"),
    ]

    code = re.sub(r";;.*", "", code)
    regex = '|'.join('(?P<%s>%s)' % pair for pair in tokens)

    for token in re.finditer(regex, code):
        yield Token(token.lastgroup, token.group())

    return [Token('INVALIDA', 'valor inválido')]