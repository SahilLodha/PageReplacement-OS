from main import Frame

# simulation LRU
page_sequence = input("Enter the page sequence [P1 P2 P3 P4 .... PN]:")
page_sequence_list = page_sequence.split(' ')
page_sequence_list = [page.strip() for page in page_sequence_list if page != '']
n_frames = int(input("Enter the number of Frames: "))

page_hits = 0
page_miss = 0

print('<--------------------------->')
print(f"Simulating for {n_frames} frames: ")
frame_obj = Frame(n_frames)
recently_used = []

for page in page_sequence_list:
    if page in frame_obj.frames.values():
        recently_used.remove(page)
        page_hits += 1
        recently_used.append(page)
    else:
        if len(recently_used) < n_frames:
            recently_used.append(page)
            for key in frame_obj.frames.keys():
                if frame_obj.frames[key] == '':
                    frame_obj.frames[key] = page
                    break
        else:
            least_recent_used = recently_used.pop(0)
            recently_used.append(page)
            for key in frame_obj.frames.keys():
                if frame_obj.frames[key] == least_recent_used:
                    frame_obj.frames[key] = page
                    break

        page_miss += 1
    print(frame_obj)