from main import Frame

page_sequence = input("Enter size of input as [P1 P2 P3 ...... PN]: \n")
page_sequence_list = page_sequence.upper().split(' ')
page_sequence_list = [page.strip() for page in page_sequence_list if page != '']
page_miss = 0
page_hits = 0

frame_three = Frame(3)
frame_four = Frame(4)

print("Simulating for three frames: ")
for page in page_sequence_list:
    flag = 0
    for frame in frame_three.frames.keys():
        if page == frame_three.frames[frame]:
            page_hits += 1
            flag = 1
    if flag == 0:
        position = page_miss % 3
        key_dict = f'F{position}'
        page_miss += 1
        frame_three.frames[key_dict] = page

    print(frame_three)

print("Results for 3 Frame: ")
print(f"Page Hits: {page_hits}\nPage Miss: {page_miss}")

# Rebooting for 4 frames
page_miss = 0
page_hits = 0

print("Simulating for four frames: ")
for page in page_sequence_list:
    flag = 0
    for frame in frame_four.frames.keys():
        if page == frame_four.frames[frame]:
            page_hits += 1
            flag = 1
    if flag == 0:
        position = page_miss % 4
        key_dict = f'F{position}'
        page_miss += 1
        frame_four.frames[key_dict] = page

    print(frame_four)

print("For four frames: ")
print(f"Page Hits: {page_hits}\nPage Miss: {page_miss}")