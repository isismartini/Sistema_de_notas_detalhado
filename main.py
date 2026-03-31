notas=[ ]
contagem_categorias= {
    "Excelente": 0,
    "Bom": 0,
    "Recuperação": 0,
    "Reprovados" : 0,
}
print("--- Registro de Notas (25 Alunos) ---")
for i in range(1,26):
    while True:
        try:
            nota = float(input(f"digite a nota do aluno {i}: "))
            if 0 <= nota <= 10:
                notas.append(nota)
                
                if nota >= 9:
                    contagem_categorias["Excelente"]
                elif nota >=7:
                    contagem_categorias["Bom"]
                elif nota >=5:
                    contagem_categorias["Recuperação"]
                else:
                    contagem_categorias["reprovado"]
                break
            else:
                print("Por favor, digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
