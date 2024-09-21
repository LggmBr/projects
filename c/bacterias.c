#include <stdio.h>

int main() {
  int N, P, Q, D;

  scanf("%d", &N);
  scanf("%d", &P);

  D = 1;
  Q = P;

  while (1) {
    Q = Q*P;
    if (Q>N) {
      break;
    } else {
      D = D + 1;
    }
  }
  printf("%d\n", D);
  return 0;
}
