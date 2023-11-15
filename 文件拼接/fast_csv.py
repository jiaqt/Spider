import csv


def fast_csv():
    fasta_file_path = "../files/H3N2.fasta"  # 替换为您的FASTA文件路径
    fasta_file_path = "../files/H1N1.fasta"  # 替换为您的FASTA文件路径
    csv_file_path = "H1N1_output.csv"     # 替换为您想要保存CSV文件的路径

    sequences = []  # 用于存储序列信息的列表
    current_sequence = ""  # 用于存储当前序列的临时变量
    with open(fasta_file_path, "r") as fasta_file:
        for line in fasta_file:
            line = line.strip()
            if line.startswith(">"):  # 标识行
                if current_sequence:   # 保存之前的序列信息
                    sequences.append(current_sequence)
                current_sequence = line + " "  # 将标识行作为序列信息的一部分
            else:
                current_sequence += line

    # 处理最后一个序列
    if current_sequence:
        sequences.append(current_sequence)

    # 将序列信息写入CSV文件
    with open(csv_file_path, "w", newline="") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["ID", "Sequence"])  # 写入CSV文件的标题行
        for idx, sequence in enumerate(sequences, start=1):
            csv_writer.writerow([f"Sequence{idx}", sequence])

    print("FASTA文件已成功转换为CSV文件。")



fast_csv()



input_csv_path = "H1N1_output.csv"    # 替换为您的CSV文件路径
output_csv_path = "H1N1.csv"  # 替换为您想要保存的CSV文件路径

def process_sequence(sequence):
    index = sequence.find("[")  # 查找 "[" 的位置
    if index != -1:
        sequence = sequence[index+1:]  # 删除 "[" 前面的内容
    return sequence.strip()

# 处理CSV文件
with open(input_csv_path, "r") as input_csv, open(output_csv_path, "w", newline="") as output_csv:
    csv_reader = csv.reader(input_csv)
    csv_writer = csv.writer(output_csv)

    for row in csv_reader:
        if len(row) == 2:  # 确保每行有两列
            sequence_id = row[0]
            sequence_data = process_sequence(row[1])
            csv_writer.writerow([sequence_id, sequence_data])

print("处理完成。")

