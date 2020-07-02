//Day12-2
listnode* reverseBetween(listnode* A, int m, int n) {
    listnode *p,*b;
    p=A;
    b=A;
    if(p==NULL) return NULL;
    if(n<m) return A;
    int i;
    for(i=1;i<m;i++) {
        if(p->next!=NULL) p=p->next;
        else return A;
    }
    for(i=1;i<m-1;i++) b=b->next;
    int c=0;
    listnode *q,*r,*nxt,*curr;
    q=NULL;
    nxt=NULL;
    curr=p;
    r=A;
    for(i=1;i<=n;i++) {
        r=r->next;
    }
    while(curr!=NULL&&c!=(n-m+1)) {
        q=curr;
        nxt=curr->next;
        q->next=r;
        r=q;
        curr=nxt;
        c++;
    }
    if(m!=1) {
        b->next=r;
        return A;
    }
    else return r;
}

