#include "unif01.h"
#include "ufile.h"
#include "bbattery.h"

int main (int argc, char *argv[])
{
	unif01_Gen *gen1;
	gen1 = ufile_CreateReadText (argv[1], 1);
	bbattery_Crush(gen1);
	ufile_DeleteReadText(gen1);
}