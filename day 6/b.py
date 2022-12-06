# variable to store answer lol
first_marker = 0

with open('./input.txt', 'r') as input:
    # grab line from input file
    data_stream = input.read()

    # using enumerate cause i want both the index and the data
    for index, data in enumerate(data_stream):
        try:
            # collect 14 chars from current index into a chunk
            chunk = [data_stream[i + index] for i in range(14)]

            # convert chunk to a set and check if it still contains 14 chars
            if len(set(chunk)) == len(chunk):

                # set first marker to the index of the last item in the chunk
                first_marker = index + 14
                break

        # just cause the error is we are going to at some point access beyond the data_stream
        except IndexError:
            pass
    # output
    print(first_marker)
