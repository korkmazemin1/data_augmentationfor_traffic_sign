def label_copier(input_file_path,output_path):
    # Giriş dosyasını oku
    output_path=output_path.replace(".jpg",".txt")
    with open(input_file_path, 'r') as infile:
        content = infile.read()
    
    # İçeriği yeni bir dosyaya yaz
    with open(output_path, 'w') as outfile:
        outfile.write(content)

