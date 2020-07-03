#Day13-1
listnode* deleteDuplicates(listnode* A) {
    listnode* ptr=A,*temp;
    while(ptr->next!=NULL){
        if(ptr->val==ptr->next->val){
            temp=ptr->next->next;
            free(ptr->next);
            ptr->next=temp;
        }
        else ptr=ptr->next;
    }
    return A;
}