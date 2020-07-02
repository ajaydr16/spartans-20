//Day12-1
listnode* mergeTwoLists(listnode* A, listnode* B) {
    listnode *ans,*ptr1=A,*ptr2=B;
    if(A==NULL)         return B;
    if(B==NULL)         return A;
    if(A->val<B->val)
    {
        ans=A;
        ptr1=ptr1->next;
    }
    else
    {
        ans=B;
        ptr2=ptr2->next;
    }
    while(ptr1 && ptr2)
    {
        if(ptr1->val<ptr2->val)
        {
            ans->next=ptr1;
            ans=ptr1;
            ptr1=ptr1->next;
        }
        else
        {
            ans->next=ptr2;
            ans=ptr2;
            ptr2=ptr2->next;
        }
    }
    if(ptr2)
    ans->next=ptr2;
    else
    ans->next=ptr1;
    if(A->val<B->val)       return A;
    else                    return B;
}