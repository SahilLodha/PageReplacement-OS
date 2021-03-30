from main import Frame

n_frame = int(input("Enter the no of frames: "))
frame_obj = Frame(n_frame)
page_sequence = input("Enter the frame sequence [P1 P2 P3 P4 P5 ... PN]: ")
page_sequence_list = page_sequence.split(' ')
page_sequence_list = [page.strip() for page in page_sequence_list if page != '']
page_hits = 0
page_miss = 0

for idx, page in enumerate(page_sequence_list):
    if page in frame_obj.frames.values():
        page_hits += 1
    else:
        page_miss += 1
        for frame, value in frame_obj.frames.items():
            if value == '':
                frame_obj.frames[frame] = page
                break
        else:
            remaining_pages = []
            for rpage in page_sequence_list[idx + 1:]:
                if rpage not in remaining_pages:
                    remaining_pages.append(rpage)
                if len(remaining_pages) == n_frame:
                    break
            for frame, value in frame_obj.frames.items():
                if value not in remaining_pages:
                    frame_obj.frames[frame] = page
                    break
            else:
                last_page = remaining_pages[-1]
                for frame, value in frame_obj.frames.items():
                    if value == last_page:
                        frame_obj.frames[frame] = page
    print(frame_obj)

print('Page Hits:', page_hits)
print('Page Miss:', page_miss)





