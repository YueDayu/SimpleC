var ch_new=new Array(1003);
function check1(x) { 
  var p=0;
  if (x=='*'||x=='/') 
    p=3;
  else if (x=='+'||x=='-') 
    p=2;
  else if (x==')') 
    p=1;
  else if (x=='(') 
    p=4;
  return p;
} 
function check2(x) { 
  var p=0;
  if (x=='*'||x=='/') 
    p=3;
  else if (x=='+'||x=='-') 
    p=2;
  else if (x==')') 
    p=4;
  else if (x=='(') 
    p=1;
  return p;
} 
function ChangeToBehind(ch) { 
  var len=strlen(ch), num=0, l=0, i, j, top=0;
  var heap=new Array(2000);
  ch_new[0]=0;
  heap[0]='#';
  ch[len]='#';
  for (i=0; i<=len; i++){ 
    if (ch[i]>='0'&&ch[i]<='9') 
      num++;
    else { 
      for (j=0; j<num; j++)
        ch_new[l+j]=ch[i-num+j];
      ch_new[l+num]=' ';
      l=l+num+1;
      num=0;
      while (check1(ch[i])<=check2(heap[top])){ 
        if (top==0)         break;
        if (heap[top]!='(') { 
          ch_new[l]=heap[top];
          l=l+1;
        } 
        else if (ch[i]==')') { 
          top--;
          break;
        } 
        top--;
      } 
      heap[++top]=ch[i];
    } 
  } 
} 
function getResult(ch) { 
  var len=strlen(ch);
  var top=0, num=0, i, flag=0;
  var sta=new Array(1003);
  for (i=0; i<len; i++){ 
    if (ch[i]>='0'&&ch[i]<='9') { 
      flag=1;
      num=num*10+ch[i]-'0';
    } 
    else { 
      if (flag==1) { 
        sta[top]=num;
        top=top+1;
      } 
      num=0;
      flag=0;
      if (ch[i]=='+') { 
        top=top-1;
        sta[top-1]=sta[top-1]+sta[top];
      } 
      else if (ch[i]=='-') { 
        top=top-1;
        sta[top-1]=sta[top-1]-sta[top];
      } 
      else if (ch[i]=='*') { 
        top=top-1;
        sta[top-1]=sta[top-1]*sta[top];
      } 
      else if (ch[i]=='/') { 
        top=top-1;
        sta[top-1]=sta[top-1]/sta[top];
      } 
    } 
  } 
  return sta[0];
} 
function test(ch) { 
  ChangeToBehind(ch);
  printf("%lf\n",getResult(ch_new));
} 
function main() { 
  var ch="1+(5-2)*4/(2+1)";
  test(ch);
  return 0;
} 
function printf(str) {
  if (arguments.length > 1)
    console.log(str, arguments[1]);
  else
    console.log(str);
}
function strlen(ch) {
  return ch.length;
}
main();