import matplotlib.pyplot as plt
import matplotlib.animation as animate
#import os
#import shutil
#import os.path
#from os import path



Writer = animate.writers['ffmpeg']
writer = Writer(fps=10, metadata=dict(artist='Me'), bitrate = 1800)



def bubble(A,n,title):
    def swap(A, i, j):

        for x in range(n):
            bar_rects[x].set_color('b')

        if i != j:
            A[i], A[j] = A[j], A[i]
        bar_rects[i].set_color('r')
        bar_rects[j].set_color('r')



    def BubbleSort(A):
        if n == 1:
            return

        for i in range(n - 1):
           for j in range(n - 1 - i):

                if A[j] > A[j + 1]:

                    swap(A, j, j + 1)
                yield A
        yield A

    fig,ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)),A,align='edge')

    text = ax.text(0.02,0.95,"",transform=ax.transAxes)

    iteration = [0]


    generator = BubbleSort(A)

    def update_fig(A,rects, iteration):
        for rect, val in zip(rects,A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text('No of Iterations: {}'.format(iteration[0]))

    anim = animate.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,iteration),frames=generator, interval=10000, repeat= True, save_count = 20000,repeat_delay=10000)


    anim.save('/home/Manjunath/deploy/static/%s.mp4'%title, writer=writer)

def insert(A,title):

    def swap(A, i, j):

        for x in range(len(A)):
            bar_rects[x].set_color('b')

        if i != j:
            A[i], A[j] = A[j], A[i]
        bar_rects[i].set_color('r')
        bar_rects[j].set_color('r')

    def insertionsort(A):
        for i in range(1, len(A)):
            j = i
            while j > 0 and A[j] < A[j - 1]:
                swap(A, j, j - 1)
                j -= 1
                yield A
            for w in range(20):
                yield A

    fig,ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)),A,align='edge')

    text = ax.text(0.02,0.95,"",transform=ax.transAxes)

    iteration = [0]


    generator = insertionsort(A)

    def update_fig(A,rects, iteration):
        for rect, val in zip(rects,A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text('No of Iterations: {}'.format(iteration[0]))

    anim = animate.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,iteration),frames=generator, interval=10000, repeat= True, save_count = 20000,repeat_delay=10000)


    anim.save('/home/Manjunath/deploy/static/%s.mp4'%title, writer=writer)

def quick(A,start,end,title):
    def swap(A, i, j):

        for x in range(len(A)):
            bar_rects[x].set_color('b')

        if i != j:
            A[i], A[j] = A[j], A[i]
        bar_rects[i].set_color('r')
        bar_rects[j].set_color('r')



    def quicksort(A, start, end):


        if start >= end:
            return

        pivot = A[end]
        pivotIdx = start

        for i in range(start, end):
            if A[i] < pivot:
                swap(A, i, pivotIdx)
                pivotIdx += 1
            yield A
        swap(A, end, pivotIdx)
        yield A

        yield from quicksort(A, start, pivotIdx - 1)
        yield from quicksort(A, pivotIdx + 1, end)
        for w in range(20):
            yield A

    fig,ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)),A,align='edge')

    text = ax.text(0.02,0.95,"",transform=ax.transAxes)

    iteration = [0]


    generator = quicksort(A,start,end)

    def update_fig(A,rects, iteration):
        for rect, val in zip(rects,A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text('No of Iterations: {}'.format(iteration[0]))

    anim = animate.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,iteration),frames=generator, interval=10000, repeat= True, save_count = 20000,repeat_delay=10000)


    anim.save('/home/Manjunath/deploy/static/%s.mp4'%title, writer=writer)

def select(A,title):
    def swap(A, i, j):

        for x in range(len(A)):
            bar_rects[x].set_color('b')

        if i != j:
            A[i], A[j] = A[j], A[i]
        bar_rects[i].set_color('r')
        bar_rects[j].set_color('r')

    def selectionsort(A):
        if len(A) == 1:
            return

        for i in range(len(A)):
            minVal = A[i]
            minIdx = i
            for j in range(i, len(A)):
                if A[j] < minVal:
                    minVal = A[j]
                    minIdx = j
                yield A
            swap(A, i, minIdx)
            yield A
        for w in range(20):
            yield A


    fig,ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)),A,align='edge')

    text = ax.text(0.02,0.95,"",transform=ax.transAxes)

    iteration = [0]


    generator = selectionsort(A)

    def update_fig(A,rects, iteration):
        for rect, val in zip(rects,A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text('No of Iterations: {}'.format(iteration[0]))

    anim = animate.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,iteration),frames=generator, interval=10000, repeat= True, save_count = 20000,repeat_delay=10000)


    anim.save('/home/Manjunath/deploy/static/%s.mp4'%title, writer=writer)

def MERGE(A,start,end,title):
    def mergesort(A, start, end):

        if end <= start:
            return

        mid = start + ((end - start + 1) // 2) - 1
        yield from mergesort(A, start, mid)
        yield from mergesort(A, mid + 1, end)
        yield from merge(A, start, mid, end)
        for x in range(len(A)):
            bar_rects[x].set_color('b')
        yield A
        for w in range(10):
            yield A

    def merge(A, start, mid, end):

        merged = []
        leftIdx = start
        rightIdx = mid + 1
        bar_rects[leftIdx].set_color('r')
        bar_rects[rightIdx].set_color('r')

        while leftIdx <= mid and rightIdx <= end:
            if A[leftIdx] < A[rightIdx]:
                merged.append(A[leftIdx])
                leftIdx += 1
            else:
                merged.append(A[rightIdx])
                rightIdx += 1

        while leftIdx <= mid:
            merged.append(A[leftIdx])
            leftIdx += 1

        while rightIdx <= end:
            merged.append(A[rightIdx])
            rightIdx += 1

        for i, sorted_val in enumerate(merged):
            A[start + i] = sorted_val
            yield A
    fig,ax = plt.subplots()
    ax.set_title(title)

    bar_rects = ax.bar(range(len(A)),A,align='edge')

    text = ax.text(0.02,0.95,"",transform=ax.transAxes)

    iteration = [0]


    generator = mergesort(A,start,end)

    def update_fig(A,rects, iteration):
        for rect, val in zip(rects,A):
            rect.set_height(val)
        iteration[0] += 1
        text.set_text('No of Iterations: {}'.format(iteration[0]))

    anim = animate.FuncAnimation(fig, func=update_fig, fargs=(bar_rects,iteration),frames=generator, interval=10000, repeat= True, save_count = 20000,repeat_delay=10000)


    anim.save('/home/Manjunath/deploy/static/%s.mp4'%title, writer=writer)
