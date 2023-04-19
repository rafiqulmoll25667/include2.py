#include <stdio.h>

int main() {
   float distance, time, velocity;

   printf("Введите расстояние (в метрах): ");
   scanf("%f", &distance);

   printf("Введите время (в секундах): ");
   scanf("%f", &time);

   velocity = distance / time;

   printf("Средняя скорость света в воздухе: %.2f м/с\n", velocity);

   return 0;
}
