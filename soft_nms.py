def temporal_nms(bboxes, thresh):
    """
    One-dimensional non-maximal suppression
    :param bboxes: [[st, ed, score, ...], ...]
    :param thresh:
    :return:
    """
    #t1 = bboxes[:, 0]
    #t2 = bboxes[:, 1]
    #scores = bboxes[:, 2]
    #print(t1.shape)
    #print(t2.shape)
    #print("scores",scores.shape)

    #durations = t2 - t1
    #order = scores.argsort()[::-1]
    #print(durations.shape)
    #print(order.shape)

    #keep = []
    #while order.size > 0:
    #    i = order[0]
    #    keep.append(i)
    #    tt1 = np.maximum(t1[i], t1[order[1:]])
    #    tt2 = np.minimum(t2[i], t2[order[1:]])
    #    intersection = tt2 - tt1
    #    IoU = intersection / (durations[i] + durations[order[1:]] - intersection).astype(float)

    #    print("tt1",tt1.shape)
    #    print("IoU",IoU.shape)



    #    inds = np.where(IoU <= thresh)[0]
    #    order = order[inds + 1]
 #    print("inds",inds.shape)
    #    print("order,",order.shape)

    #print("keep",len(keep))
    #return bboxes[keep, :]
    scores = bboxes[:, 2]
    keep = []
    s = bboxes[:,0].size
    ctr = 0
    while len(keep)<s:
        ctr+=1
        print(ctr)
        t1 = bboxes[:,0]
        t2 = bboxes[:,1]
        scores = bboxes[:,2]
        order = scores.argsort()[::-1]
        i = order[0]
        print(bboxes.shape)
        keep.append(bboxes[i,:])
        dur = t2-t1
        tt1 = np.maximum(t1[i], t1[order])
        tt2 = np.minimum(t2[i], t2[order])
        inter = tt2-tt1
        IoU = inter / (dur[i] + dur - inter).astype(float)
        print(IoU.shape,scores.shape)
        inds = np.where(IoU >= thresh)[0]
#        scores[inds] = scores[inds] * (1 - IoU)
#        scores = np.delete(scores,i)i
        inds = inds[inds>=len(IoU)]
        scores[inds+1] = scores[inds+1] * (1 - IoU[inds])
        #scores = np.delete(scores,i)
        #t1 = np.delete(bboxes[:,0],i)
        #t2 = np.delete(bboxes[:,1],i)
        bboxes = np.delete(bboxes,(i),axis = 0)

    print("shape of keep",len(keep))
    return np.array(keep)

