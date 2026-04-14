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
                    contagem_categorias["Excelente"] += 1
                elif nota >= 7:
                    contagem_categorias["Bom"] += 1
                elif nota >= 5:
                    contagem_categorias["Recuperação"] += 1
                else:
                    contagem_categorias["Reprovados"] += 1
                break
            else:
                print("Por favor, digite uma nota válida entre 0 e 10.")
        except ValueError:
            print("Entrada inválida. Digite um número.")
            
media_geral = sum(notas) / len(notas)
maior_nota = max(notas)
menor_nota = min(notas)

print("\n" + "=" * 30)
print("RELATORIO FINAL DA TURMA")
print("=" * 30)
print(f"Media Geral da Turma: {media_geral:.2f}")
print(f"Maior Nota: {maior_nota:.2f}")
print(f"Menor Nota: {menor_nota:.2f}")
print("-" * 30)
print("DISTRIBUICAO POR CATEGORIA:")

for categoria, total in contagem_categorias.items():
    print(f"- {categoria}: {total} aluno(s)")
